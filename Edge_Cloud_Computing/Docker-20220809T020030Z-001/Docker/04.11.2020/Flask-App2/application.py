from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcomemessage():
    return "Welcome to the world of containers !!"

@app.route("/welcome")
def index():
   return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4500, debug=True)
    