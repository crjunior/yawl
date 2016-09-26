import webapp2

class PingService(webapp2.RequestHandler):
    """ Health check API """
    def get(self):
        self.response.body = 'ping_service'

APP = webapp2.WSGIApplication([
    ('/api/ping', PingService)
])
