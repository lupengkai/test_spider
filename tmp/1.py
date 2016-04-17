import urllib.request
import urllib

with urllib.request.urlopen('http://baidu.com') as f:
    data = f.read()
    print(data.decode('utf-8'))
