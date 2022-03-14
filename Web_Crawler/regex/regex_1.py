import re

content = 'Hello World!'

res_1 = re.match('\w{5}', content)

print(res_1.group())
