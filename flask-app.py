from flask import Flask,render_template
app=Flask(__name__)


posts=[
{
'author':'Deepanshu Yadav',
'title':'BLOG POST',
'content':'First Blog Post',
'date_posted':'April 18 2024'
},
{
'author':'Sam manic',
'title':'BLOG POST',
'content':'First Blog Post',
'date_posted':'August 18 2024'
}
]


@app.route("/")
@app.route("/home")
def home():
        return render_template("home.html",posts=posts)



@app.route("/track")
def track():
        return render_template("track.html")

@app.route("/about")
def about():
	return render_template("about.html")
