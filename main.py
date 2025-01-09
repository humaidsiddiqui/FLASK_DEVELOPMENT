from flask import Flask
app=Flask(__name__)
@app.route("/home")
def hello():
        print("welcome to the world of python")
        return "Hi FROM AWS SERVER RUNNING BEHIND NGINX PROXY SERVER"
#app.run(host="0.0.0.0",port=8080)
