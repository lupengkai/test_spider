import requests
from bs4 import BeautifulSoup
import logging

from collections import deque
import login_rs_2
import re

re_rs = re.compile(r'.*forum\.php\?mod=viewthread&tid=\d{6}$')

save_path = '/home/tage/Documents/spider/temp.out'
f = open(save_path, 'w')

queue = deque()
visited = set()

session = requests.Session()
login_rs_2.login(session=session)
url = 'http://rs.xidian.edu.cn/bt.php?mod=browse&c=10'

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问
    print('已抓取： ' + str(cnt) + ' 正在抓取 <---   ' + url)
    cnt += 1
    try:
        response = session.get(url, timeout=2)
        if 'html' not in response.headers['content-type']:
            continue
        soup = BeautifulSoup(response.text)

        content = soup.find(name='td', id=re.compile('postmessage'))
        if content:
            title = soup.title.text
            if title.startwith('[电影]'):
                f.write(content.text)
        if soup.find('base'):
            base_href = soup.find('base')['href']
        print('BASE: ', base_href)
        for x in soup.find_all('a'):
            if 'href' in x.attrs:
                f_url = x['href']
                print(f_url)

                if f_url not in visited and re_rs.match(f_url):
                    print('Matched', f_url)
                    loc_http = f_url.find('http')
                    if loc_http == 0:
                        queue.append(f_url)
                        print('加入队列 ---> ' + f_url)
                    else:
                        loc_dot = f_url.find('.')
                        if loc_dot == 0:
                            f_url = f_url[2:]

                        f_url = base_href + f_url
                        queue.append(f_url)
                        print('加入队列 ---> ' + f_url)




    except KeyboardInterrupt as e:
        f.flush()
        f.close()
        exit()
    except Exception as e:
        logging.exception(e)
        continue
