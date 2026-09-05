# print("Hello Manipriyan!!")

from flask import Flask

app = Flask("My First Flask App")

@app.route("/")

def Index():
    return "Hello from flask app"

@app.route("/aboutme")

def About():
    return "<h1> Hello My name is Manipriyan, I will become a senior software architect who earns 1Crore per year salary before 2028 </h1>"

app.run(debug=True)