from flask import Flask 
app=Flask(__name__)


@app.route("/")
@app.route("/home")
<<<<<<< HEAD
def home():
	return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #343a40;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Flask App!</h1>
        <p>This is a basic HTML page served by Flask.</p>
    </div>
</body>
</html>
'''
