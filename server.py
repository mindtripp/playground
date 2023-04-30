from flask import Flask, render_template


app = Flask(__name__)


@app.route('/play')
def one():
    return render_template("index.html",num=5,colors=["red", "green", "blue"])

@app.route('/play/<int:num>')
def ltwo(num):
    return render_template("index.html", num=num,colors=["red", "green", "blue"])

@app.route('/play/<int:num>/<string:color>')
def three(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True) 