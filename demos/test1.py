import base64

b = base64.b64encode('ten@qq.com:123456'.encode('ascii'))
print(b)
