import requests as req

class Get:
    def __init__(self, url):
        self.url = url
    
    def makeGet(self):
        output = req.get(self.url)
        inbound = output.text
        print(inbound)
    
coinflip = Get("http://flipacoinapi.com/txt")
coinflip.makeGet()