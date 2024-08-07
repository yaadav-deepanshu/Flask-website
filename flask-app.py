from flask import Flask,render_template 
app=Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")



@app.route("/track")

def track():
	return render_template("track.html")
