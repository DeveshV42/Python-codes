from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home():  
    return render_template("home2.html")  
 
@app.route('/signin2')  
def signin():  
    return render_template("signin2.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == '123456':  
        return redirect(url_for("success"))  
    return redirect(url_for("signin2"))  
 
@app.route('/success')  
def success():  
    return "logged in successfully"  
  
if __name__ == '__main__':  
    app.run(debug = True)  