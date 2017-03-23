create table psql_translate.cache(
    id bigserial primary key,
    source char(2) not null,
    target char(2) not null,
    q text not null,
    result psql_translate.response not null,
    created timestamp not null default now(),
	api varchar(20)
);
create unique index u_cache_q_source_target_api on psql_translate.cache
    using btree(md5(q), source, target, api);

comment on table psql_translate.cache is 'Cache for psql translate calls';

create or replace function psql_translate.google(source char(2), target char(2), q text) returns text as $$
#variable_conflict use_variable
declare
	res psql_translate.response;
begin

    if current_setting('google.api_key') is null or current_setting('google.api_key') = '' then
        raise exception 'Configuration error: google.api_key has not been set.';
    end if;

	res := (select result
		from psql_translate.cache as c
		where md5(trim(c.q)) = md5(q) and c.source = source and c.target = target
		and c.api = 'google');

	if res.success then
	   return res.message;
	end if;

	res = psql_translate.py_google(
		current_setting('google_translate.api_key'), source, target, q);

	if not res.success then
	   raise exception 'Failed: %, query: %', res.message, q;
	else
	   insert into psql_translate.cache(source, target, q, result, api)
	   values(source, target, q, res, 'google');

	end if;

	return res.message;
end;
$$ language plpgsql;
