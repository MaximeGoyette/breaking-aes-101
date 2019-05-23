import base64
import requests
import string

url = 'http://localhost:5001/api/encrypt'
block_size = 16
alphabet = string.printable

def make_request(data):
    r = requests.post(url, headers={'Content-Type': 'application/json'}, json={'data': base64.b64encode(data)})
    return base64.b64decode(r.text)


def get_padding_len():
    i = 0
    l = None

    while True:
        token = make_request('a'*i)
        token_len = len(token)

        if l and token_len != l:
            return l
        else:
            l = token_len

        i += 1


def get_blocks(s, hexa=True):
    a = [s[i:i+block_size] for i in xrange(0, len(s), block_size)]
    if hexa:
        return [x.encode('hex') for x in a]
    else:
        return a


def solve(l, original_len):
    s = 'a'*(l*block_size - 1)
    flag = ''

    for i in xrange(l*block_size):
        target = get_blocks(make_request(s[i:]))

        for c in alphabet:
            token = make_request(s[i:] + flag + c)
            blocks = get_blocks(token)

            if target[l - 1] == blocks[l - 1]:
                flag += c
                print flag
                break

    return flag


def prettify(s, hexa=True):
    return ''.join(get_blocks(s, hexa))


if __name__ == '__main__':
    padding_len = get_padding_len()
    solve(padding_len//block_size, padding_len)