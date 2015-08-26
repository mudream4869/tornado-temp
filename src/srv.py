import tornado.ioloop
import tornado.web
import tornado.template

import config

import user
import session

loader = tornado.template.Loader("./templ")

class RequestHandler(tornado.web.RequestHandler):
    KEYNAME = "mmkey"

    def get_user(self):
        
        if not self.get_secure_cookie(RequestHandler.KEYNAME):
            return user.null_user
        
        key = self.get_secure_cookie(RequestHandler.KEYNAME)
        uid = session.SessionHandler.inst.getuid(key)

        if uid == None : 
            return user.null_user

        _user = user.UserHandler.inst.getUserByUserId(int(uid))
        
        if _user.is_null :
            session.SessionHandler.inst.deluid(key)
        
        return _user

    def set_user(self, _user):
        
        key = session.SessionHandler.inst.setuid(_user.id)
        self.set_secure_cookie(RequestHandler.KEYNAME, str(key))


class MainHandler(RequestHandler):
    def get(self):
        _user = self.get_user()
        self.write(
            loader.load("index.html").generate(
                user = _user
            )
        )


application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': "./static/"}),
], cookie_secret=config.secure_cookie)


if __name__ == "__main__":
    application.listen(8888)
    user.UserHandler()
    session.SessionHandler()
    tornado.ioloop.IOLoop.current().start()
