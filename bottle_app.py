from bottle import run, route, template, static_file, TEMPLATE_PATH, default_app, debug, request
from hashlib import sha256

TEMPLATE_PATH.insert(0, './pages')


# static file function
#@route("/pages/<filename>")
#def static_file_callback(filename):
#    return static_file(filename, root="./pages")




@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/C:Users/ozturk/Documents/GitHub/a2-ibrahimztrk61')


def login():
    return '<h1>on login</h1>'


# defining functions for every page

@route("/")
def index():
    return template('index')

def models():
    return template('models')

def photographs():
    return template('photographs')


route("/index", "GET", index)
route("/models", "GET", models)
route("/photographs", "GET", photographs)

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
