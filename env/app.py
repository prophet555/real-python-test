
from flask import Flask

#create application object
app = Flask(__name__) 

# use decoraters to link function to url
@app.route("/")
@app.route("/hello")

# define the view using a function , which returns a string
def hello_word():
	return "Hello, World!"

# start development server using the run() method
if __name__ == "__main__":
	app.run()

