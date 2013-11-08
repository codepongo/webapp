import sys
import os
sys.path.append(os.path.dirname(__file__))
import web
web.config.debug = True
import hello
import about
import whereisip
urls = ('/hello/(.*)', hello.hello,
        '/aboutme.*', about.me,
        '/whereisip.*', whereisip.whereisip,
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user':None})
if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
