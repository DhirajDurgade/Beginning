from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "This is my first machine learing project"

if __name__=="main":
    app.run(debug=True)
    