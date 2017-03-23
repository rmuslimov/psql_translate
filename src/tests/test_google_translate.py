# coding: utf-8

from .utils import get_env
from ..google_translate import main

ENV = get_env()


def test_api():
    value = main(
        ENV['google.api_key'],
        'ru', 'en', u'Конь'.encode('utf8')
    )
    assert value == {'message': 'Horse', 'success': True}
