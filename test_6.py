import urllib.request
import http.cookiejar

def save_file(data):
    save_path = '/home/tage/Documents/spider/temp.out'
    with open(save_path, 'wb') as f:
        f.write(data)

def makeMyOpener(head={
    'Cpnnection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,zh-CN;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for k, v in head.items():
        elem = (k, v)
        header.append(elem)
    opener.addheaders = header
    return opener

opener = makeMyOpener()
with opener.open('http://www.baidu.com', timeout=1000) as f:
    data = f.read()
    save_file(data)
    print(data.decode('utf-8'))
    for k, v in f.getheaders():
        print(k, v)

