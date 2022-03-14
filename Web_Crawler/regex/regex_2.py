import re

content_1 = 'https://baidu.com/index.html'
content_2 = 'Hello 1234567 World_This is a Regex Demo'

ret_1 = re.match('^(.*)://(.*)/(.*)$', content_1)
ret_2 = re.match('(^Hello\s(\d+)\sWorld)', content_2)
ret_3 = re.search('(?<=://).*(?=/)', content_1)

# 只能说match不行

print(ret_1.groups())
print(ret_2.group(2))
print(ret_3)