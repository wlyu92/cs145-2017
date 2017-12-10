#import web
# The URL / (i.e. the front page) to be handled by the class
    #named index
#urls = (
#    '/','index'
#)

# GET and POST: functions that Web visitors ask web servers to perform on URLs
    # GET: used to request the text of a web page
    # POST: used to submit certain kinds of forms

# This GET function will get called by web.py anytime someone makes a GET request for /.
#class index:
 #   def GET(self):
  #      return "Hello, world!"

# create an application specifying the urls and tell web.py to start serving web pages
#if __name__ == "__main__":
 #   app = web.application(urls,globals()) #tell web.py to create an application with the URLs we listed above,
  #  app.run

import web
# tells web.py to look for templates in my templates directory
render = web.template.render('templates/')

urls = (
    '/(.*)', 'index'
)

#class index:
#    def GET(self):
        # say hello to Bob
        #name = 'Bob'
        #return render.index(name)
        # let ppl enter their own name in
        # e.g. by visiting the URLs http://0.0.0.0:8080/?name=Joe
#        i = web.input(name = None)
#        return render.index(i.name)
class index:
    def GET(self, name):
        return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()