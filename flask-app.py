from flask import Flask,render_template 
app=Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/track")
def home():
	return render_template("home.html")



def track():
	return render_template("track.html")
