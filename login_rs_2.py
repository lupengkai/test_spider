import gzip
import requests


def ungzip(data):
    try:
        print('正在解压...')
        data = gzip.decompress(data)
        print('解压完毕！')
    except Exception as e:
        print('Error', e)
        print('未经压缩，无需解压')
    return data





head = {
    'Cpnnection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,zh-CN;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Referer': 'http://rs.xidian.edu.cn/bt.php?mod=browse&t=all'
}


def login(session):

    url = 'http://rs.xidian.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

    id = 'biubiu'
    password = '7234d7bea89a2ea70cfaaf9477197120'
    post_dict = {

        'username': id,
        'password': password,
        'quickforward': 'yes',
        'handlekey': 'ls'

    }

    response = session.post(url, data=post_dict, headers=head, allow_redirects=True)



if __name__ == '__main__':
    session = requests.Session()
    login(session)