import requests
from requests.utils import requote_uri
from pyquery import PyQuery as pq


class Spider():
    def __init__(self, key_word):
        self.key_word = key_word

    def start_request(self):
        url = requote_uri(
            f'http://www.51bc.net/cy/serach.php?f_key={self.encode_key()}&f_type=chengyu&f_type2=')
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Referer': 'http://www.51bc.net/cy/serach.php'}
        r = requests.get(url, headers=headers)
        content = r.content.decode('gbk')
        doc = pq(content)
        idioms = doc("u").text()
        return idioms.split(" ")

    def encode_key(self):
        return str(self.key_word.encode('gbk')).replace(
            "\\x", '%').replace("b'", '').replace("'", '')

    def get_idioms(self):
        idioms = self.start_request()
        return idioms
