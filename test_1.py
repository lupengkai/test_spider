from urllib import request

with request.urlopen('http://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data', data.decode('utf-8'))
    print(type(f))
    print(f.geturl())
    print(f.info())
    print(f.getcode())
