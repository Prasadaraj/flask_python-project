from flask import Flask , render_template 


#server to run flask properly
# set FLASK_APP=hello.py
# set FLASK_ENV=development
# set FLASK_DEBUG=1 to automatically load after any changes
#flask run
app= Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
    first_name="JohnNallie"
    return render_template("index.html", first_name=first_name) 

#def index():
    return "<h1> Hello World </h1>"
    
@app.route('/user/<name>')

def user(name):
    return render_template("user.html",name=name) 
#localhost:5000/user/John
#@app.route('/user/<name>')

#def user(name):
    return "<h1> Hello {}</h1>".format(name)
# this will work without ,format
if __name__ == "__main__":
   app.run(debug=True)
   
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error_message="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", error_message="Prasada Prasada"), 500


@app.route("/cause500")
def cause_500():
    # Example of a runtime error
    result = 1 / 0
    return str(result)
# for this to work use the below to internal error response
#ZeroDivisionError
#ZeroDivisionError: division by zero
#Traceback (most recent call last)
#File "C:\Users\Prasada\anaconda3\envs\codify\lib\site-packages\flask\app.py", line 1536, in __call__
#    return self.wsgi_app(environ, start_response)          