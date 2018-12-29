
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################
from bottle import run, route, template, static_file, TEMPLATE_PATH, default_app, debug,request
from hashlib import sha256
TEMPLATE_PATH.insert(0,'./pages')

#static file function
@route("/static/<filename>")
def statics_file_callback(filename):
    return static_file(filename, root="./pages")
#defining functions for every page
def index():
    return html('index')
def models():
    return html('models')
def photographs():
    return html('photographs')
def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page

route("/index","GET",index)
route("/models","GET",models)
route("/photographs","GET",photographs)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

