import urllib.request

url = 'http://www.baidu.com/'
req = urllib.request.Request(url, headers={
    'Cpnnection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,zh-CN;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
})

with urllib.request.urlopen(req) as f:
    data = f.read()
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print(f.status, f.reason)
    print(data.decode('utf-8'))