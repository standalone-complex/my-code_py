import urllib.request

response = urllib.request.urlopen('http://baidu.com')

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
