from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("one.html")

@app.route("/home/<name>/")
def home(name):
    return render_template("one.html",n = name) #n = key, name=value
#templates --> one.html
#render_template(define path after templates folder)
#templates --> html --> one.html
#render_template("html/one.html")

#jinja --> key, value pair
#python file --> name=simran --> name = key/variable, simran = value
#html file --> {{key}} --> {{name}}
# {% if condition %}
#  s1
#  s2
# {% endif %}

app.run(debug=True)