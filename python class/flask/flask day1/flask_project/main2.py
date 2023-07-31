from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/")

@app.route("/login/")
def login():
    return render_template("login1.html")

@app.route("/afterlogin/",methods=["POST","GET"])
def afterlogin():
    if request.method == "GET":
        return render_template("login1.html")
    elif request.method == "POST":  #{"email":email,"passwd":pass}
        email = request.form.get("email")
        password = request.form.get("passwd")
        if email:
            if password: 
                return f"{email},{password}"
            else:
                error = "Invalid password"
                return render_template("login1.html",error=error)
        else:
            error = "Invalid email"
            return render_template("login1.html",error=error)
@app.route("/signup/")
def signup():
    return render_template("signup1.html")

@app.route("/aftersignup/",methods=["POST","GET"])
def aftersignup():
    if request.method == "POST":
        print(request.form)
        email = request.form.get("email")
        password = request.form.get("password")
        gender = request.form.get("gender")
        username = email.split("@")[0]
        if email and password:
            
            return f"Email : {email},Password : {password},Gender : {gender}"
        else:
            error = "Invalid Email or password"
            return render_template("signup1.html",error=error)
    else:
        return render_template("signup1.html")

app.run(host="localhost",port=80,debug=True)