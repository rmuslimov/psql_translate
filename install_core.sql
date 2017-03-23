create or replace function test_f(value text) returns text as $$
    return 'hello world! {}'.format(value);
$$ language plpython2u volatile;
