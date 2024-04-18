from flask import Flask,request
app=Flask(__name__)

@app.route('/formlogin',methods=['post'])
def login():
    uname=request.form['uname']
    password=request.form['pass']
    if uname=="Devesh" and password=="123456":
        return "welcome %s" % uname
    else:
        return "Invalid Username And Password !"

app.run(debug=True)        
        