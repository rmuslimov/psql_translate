# coding: utf-8


def get_env():
    """Extract env from .env file."""
    with open('.env', 'r') as f:
        source = f.read()

    return dict(row.split('=') for row in source.split('\n'))
