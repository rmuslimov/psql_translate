# coding: utf-8

import os

FUNCTIONS_TO_GENERATE = (
    'google',
)

TEMPLATE = (
    'create or replace function psql_translate.py_{name}'
    '(key text, source char(2), target char(2), value text) '
    'returns psql_translate.response as $$\n'
    '{source}'
    'return main(key, source, target, value)\n'
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
