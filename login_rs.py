import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse


def ungzip(data):
    try:
        print('正在解压...')
        data = gzip.decompress(data)
        print('解压完毕！')
    except Exception as e:
        print('Error', e)
        print('未经压缩，无需解压')
    return data


def getOpener(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for k, v in head.items():
        elem = (k, v)
        header.append(elem)
    opener.addheaders = header
    return opener


head = {
    'Cpnnection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,zh-CN;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Referer': 'http://rs.xidian.edu.cn/bt.php?mod=browse&t=all'
}



url = 'http://rs.xidian.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
opener = getOpener(head)

id = 'biubiu'
password = '7234d7bea89a2ea70cfaaf9477197120'
post_dict = {

    'username': id,
    'password': password,
    'quickforward': 'yes',
    'handlekey': 'ls'

}

postData = urllib.parse.urlencode(post_dict).encode('utf-8')

with opener.open(url, postData) as f:
    data = f.read()
    data = ungzip(data)

    print(data.decode('utf-8'))

