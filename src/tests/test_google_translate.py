from ..google_translate import main


def test_api():
    value = main('ass')
    assert 'assas' == value
