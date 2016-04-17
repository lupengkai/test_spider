import urllib
import urllib.request

data = {}
data['wd'] = 'python3.5 urllib'

url_values = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
full_url = url + url_values

with urllib.request.urlopen(full_url) as f:
    data = f.read()
    print(data.decode('utf-8'))