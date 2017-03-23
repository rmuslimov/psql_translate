import json
import urllib2

URL = ('https://www.googleapis.com/language/translate'
       '/v2?key={api_key}&source={source}&target={target}&q={query}')


def get_response(api_key, source, target, query):
    req = urllib2.Request(URL.format(
        api_key=api_key, source=source, target=target, query=query))
    response = urllib2.urlopen(req).read()
    data = json.loads(response)

    return {
        'success': True,
        'message': data['data']['translations'][0]['translatedText']
    }


def main(api_key, source, target, query):
    try:
        return get_response(api_key, source, target, query)
    except Exception as exc:
        return {
            'success': False,
            'message': unicode(exc)
        }
