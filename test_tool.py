import json
from url_path_splitter import transform
def test_transform():
    value='https://example.test/a%20b'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'a b' in json.dumps(result,ensure_ascii=False)
