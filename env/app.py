
from flask import Flask

#create application object
app = Flask(__name__) 

#error handling
app.config["DEBUG"] = True

# use decoraters to link function to url
@app.route("/")
@app.route("/hello")


# define the view using a function , which returns a string
def hello_world():
	return "Hello, World!?!?!!!!!!"

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello {}".format(name)
	else:
		return "Not Found", 404

# start development server using the run() method
if __name__ == "__main__":
	app.run()

# dynamic route

