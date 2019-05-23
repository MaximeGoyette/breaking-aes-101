import base64
import requests

url = 'http://localhost:5001/api/encrypt'

def get_padding_len():
    i = 0
    l = None

    while True:
        r = requests.post(url, json={'data': base64.b64encode('a'*i)})
        token_len = len(r.text)

        if l and token_len != l:
            return i
        else:
            l = token_len

print get_padding_len()