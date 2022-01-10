from flask import Flask, render_template, jsonify, request, session, redirect, url_for
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/1page/')
def one_page():
    return render_template("1page.html")

@app.route('/2page/')
def two_page():
    return render_template("2page.html")

@app.route('/3page/')
def three_page():
    return render_template("3page.html")

@app.route('/4page/')
def four_page():
    return render_template("4page.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)