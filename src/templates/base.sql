create or replace function {name}(value text) returns text as $$
    {pycode}
$$ language plpython2u volatile;
