from flask import Flask

# create the application object
app = Flask(__name__)


# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"


@app.route("/test")
def search():
    return "Hello!"


@app.route("/test/<search_query>")
def search2(search_query):
    return "Hi, {}".format(search_query)


@app.route("/test/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"


@app.route("/name/<name>")
def name_index(name):
    if name.lower() == "bobby":
        return "Hello, {} !".format(name), 200
    else:
        return "Not found", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
