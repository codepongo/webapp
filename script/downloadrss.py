#coding:utf-8
import os
import urllib2
rssdir = 'temp'
rss = [
        ('http://codepongo.com/blog/feed', 'blog.rss', 'blog', 'static/blog.ico'),
        ('http://www.douban.com/feed/people/zhuhuotui/interests', 'douban.rss', '豆瓣', 'static/douban.ico'),
        ('http://codepongo.com/blog/application/feed', 'app.rss', 'application', 'static/blog.ico'),
        ('https://github.com/codepongo.atom', 'github.rss', 'GitHub', 'static/github.ico'),
]
def download(url, file):
    with open(os.path.join(rssdir, file), 'wb') as f:
        req = urllib2.Request(url)
        rep = urllib2.urlopen(req)
        f.write(rep.read())
        f.close()
def main():
    if not os.path.isdir(rssdir):
        os.mkdir(rssdir)
    for r in rss:
        print r[0]
        download(r[0], r[1])
    return 0

if __name__ == '__main__':
    exit(main())
