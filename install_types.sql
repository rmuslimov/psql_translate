create schema psql_translate;

create type psql_translate.response as (
    success boolean,
	message text
);
