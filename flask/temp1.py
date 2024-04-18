from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>Hello !</h1></body></html>'
    
if __name__=="_main":
 app.run(debug=True)


 # This method is not compatible