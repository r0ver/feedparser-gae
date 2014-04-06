"""A simple rss parse and printer"""

import webapp2
from lib import feedparser

URL = 'https://www.youtube.com/rss/user/VEVO/feed.rss'


class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.headers['Charset'] = 'UTF-8'
        d = self.get_feed()

        self.response.write('<html><head></head><body>')
        
        # Print the channel name
        self.response.write('<h1>' + d['feed']['title'] + '</h1>')
        self.response.write('<ul>')
        
        for i in d['entries']:
            # We extract the url and title of the video
            url = i['links'][0]['href']
            title = i['title']
            self.response.write('<li><a href="' + url  + '">')
            self.response.write(title)
            self.response.write('</li>')
            
        self.response.write('</ul>')
        self.response.write('</body></html>')
        
    def get_feed(self): 
        d = feedparser.parse(URL)
        return d


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)