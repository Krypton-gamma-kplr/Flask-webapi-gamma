from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/hello/<int:id>')
def hello_world(id):
    print(type(id)) 
    return "Hello %d" % id

@app.route('/hello/<name>')
def hello_guest(name):
    return "Hello %s" % name

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for('hello_world', id=id-1))
    else: 
        return redirect(url_for('hello_guest'))

@app.route('/login', methods=['POST','GET'])
def login():
    """
    fonction login
    """
    return render_template("page.html")

if __name__ == "__main__":
    app.run(debug=True)
