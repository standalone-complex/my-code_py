import requests

r = requests.post('http://www.baidu.com')

print(r.text)
