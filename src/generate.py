# coding: utf-8

import os

FUNCTIONS_TO_GENERATE = (
    'google_translate',
)

TEMPLATE = (
    'create or replace function {name}(value text) returns text as $$'
    '{source}'
    'return main(value)'
    '$$ language plpython2u volatile;'
)


def generate(filename):
    with open(os.path.join('src', '{}.py'.format(filename)), 'r') as f:
        source = f.read()

    return TEMPLATE.format(name=filename, source=source)


if __name__ == '__main__':
    sources = '\n'.join(
        generate(filename)
        for filename in FUNCTIONS_TO_GENERATE
    )
    with open('install_py.sql', 'w') as f:
        f.write(sources)
