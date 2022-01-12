from flask import Flask, json, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://tester:sparta@cluster0.hntfy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta


## 인덱스 페이지 ################################################################################################################################

@app.route('/')
def main():
    return render_template("index.html")


## 업로드 페이지 ################################################################################################################################

@app.route('/upload/')
def upload_page():
    return render_template("upload.html")

@app.route('/api/upload/')
def upload_pic():
    return jsonify({'msg':'업로드 완료'})

## 결과 페이지 ################################################################################################################################

@app.route('/pokedex/')
def three_page():
    # DB에서 받아올 것.
    return render_template("pokedex.html") #DB받아서 렌더템플릿할때 같이보내줄것

## 끝 ################################################################################################################################

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)