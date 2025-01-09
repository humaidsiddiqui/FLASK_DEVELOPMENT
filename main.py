from flask import Flask
app=Flask(__name__)
@app.route("/home")
def hello():
        return "Hi FROM AWS SERVER RUNNING BEHIND NGINX PROXY SERVER"
if(__name__=="__main__"):
        app.run(host="0.0.0.0",port=8080)
        
