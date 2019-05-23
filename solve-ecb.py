import base64
import requests

username = 'aaaaaaa&is_admin=true\x02\x02'

r = requests.post('http://localhost:5000/api/encrypt', headers={
        'Content-Type': 'application/json'
    }, json={
        'username': username
    })

print r.text