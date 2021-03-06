
from bottle import *
from hashlib import sha256


TEMPLATE_PATH.insert(0, './pages')


# static file function
@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./pages")


def login():
    return '<h1>on login</h1>'

@route("/")
# defining functions for every page

@route("/index.html")
def index():
    return template('index.html')


@route("/models.html")
def models():
    return template('models.html')


@route("/photographs.html")
def photographs():
    return template('photographs.html')


def htmlify(title, text):
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

    """ % (title, text)
    return page



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

from bottle import *
from hashlib import sha256


TEMPLATE_PATH.insert(0, './pages')


# static file function
@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./pages")


def login():
    return '<h1>on login</h1>'

@route("/")
# defining functions for every page

@route("/index.html")
def index():
    return template('index.html')


@route("/models.html")
def models():
    return template('models.html')


@route("/photographs")
def photographs():
    return template('photographs')


def htmlify(title, text):
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

    """ % (title, text)
    return page



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

