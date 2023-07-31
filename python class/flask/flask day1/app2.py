from flask import Flask,render_template
app = Flask(__name__) 
@app.route("/")

@app.route("/<name>/<float:m>/<float:n>/<float:o>/")

def percent(name,m,n,o):
    sum=((m+n+o)//3)
    if sum>=90 and sum<=100:
        return f"<h1 style='background:linear-gradient( #FDFDFE,#7BD4F5);height:100%;font-size:50px;color:#2C3F85;'>{name} has got {sum}% and  grade O</h1>"
    elif sum>=80 and sum<=89:
        return f"<h1 style='background:linear-gradient( #FDFDFE,#7BF594);height:100%;font-size:50px;color:#2C3F85;'>{name} has got {sum}% and  grade E</h1>"
    elif sum>=70 and sum<=79:
        return f"<h1 style='background:linear-gradient( #FDFDFE,#F1F57B);height:100%;font-size:50px;color:#2C3F85;'>{name} has got {sum}% and  grade A</h1>"  
    elif sum>=60 and sum<=69:
        return f"<h1 style='background:linear-gradient( #FDFDFE,#F5B27B);height:100%;font-size:50px;color:#2C3F85;'>{name} has got {sum}% and  grade B</h1>" 
    elif sum>=50 and sum<=59:
        return f"<h1 style='background:linear-gradient( #FDFDFE,#7B90F5);height:100%;font-size:50px;color:#2C3F85;'>{name} has got {sum}% and  grade C</h1>" 
    elif sum>=40 and sum<=49:
        return f"<h1 style='background:linear-gradient( #FDFDFE,#EF4AC2);height:100%;font-size:50px;color:#2C3F85;'>{name} has got {sum}% and  grade D</h1>"
    else:
        return f"<h1 style='background:linear-gradient( #FDFDFE,#E7262F);height:100%;font-size:50px;color:#2C3F85;'>{name} has got {sum}% and grade F</h1>"
app.run(host="localhost",port=80,debug=True)