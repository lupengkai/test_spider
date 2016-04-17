import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'http://awesome.datwobee.com'

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问

    print('已抓取： ' + str(cnt) + ' 正在抓取 <---   ' + url)
    cnt += 1
    try:
        with urllib.request.urlopen(url, timeout=2) as urlop:
            if 'html' not in urlop.getheader('Content-Type'):
                continue
            data = urlop.read().decode('utf-8')
            linkre = re.compile('href=\"(.+?)\"')
            for x in linkre.findall(data):
                if 'http' in x and x not in visited:
                    queue.append(x)
                    print('加入队列 ---> ' + x)
    except Exception as e:
        print('Error: ', e)
        continue

