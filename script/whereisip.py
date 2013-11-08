import sys
import os
import web
import ip2nation
import qqwry
class whereisip:
    def renderPage(self, ip):
        qqwrypath = os.path.join(os.path.dirname(__file__), 'QQWry.Dat')
        qqwryinfo = ('%s %s') % qqwry.IPInfo(qqwrypath).getIPAddr(ip)
        n = ip2nation.nation(ip)
        if len(n) != 0:
            nationinfo = str(ip2nation.nation(ip)[0][0])
        else:
            nationinfo = 'unknow'
        templates = os.path.join(os.path.dirname(__file__), 'templates')
        render = web.template.render(templates)
        return render.whereisip(ip, qqwryinfo, nationinfo)
    def GET(self):
        ip = web.ctx.ip
        return self.renderPage(ip)
    def POST(self):
        print web.input()
        if web.input().ip != '':
            ip = web.input().ip
        else:
            ip = web.ctx.ip
        return self.renderPage(ip)
