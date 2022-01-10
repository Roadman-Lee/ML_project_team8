from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

import requests
import gridfs
import codecs

from pymongo import MongoClient
client = MongoClient('mongodb+srv://tester:sparta@cluster0.hntfy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

fs = gridfs.GridFS(db)


@app.route('/')
def main():
    return render_template("index.html")

## 1페이지 ################################################################################################################################

@app.route('/1page/')
def one_page():
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    response = r.json()
    rows = response['RealtimeCityAir']['row']
    return render_template("1page.html", rows=rows)

## 2페이지 ################################################################################################################################

@app.route('/2page/')
def two_page():
    # 무작위로 몇개만 뽑아올 때
    # img_list = list(db.mlimage.aggregate([{'$sample':{ 'size' : 3 }}]))
    
    # 전부 리스트로 가져올 때
    img_list = list(db.mlimage.find({},{'_id':False}))
    
    return render_template("2page.html", img_list = img_list)

@app.route('/fileupload', methods=['POST'])
def file_upload():
    title_receive = request.form['title_give']
    file = request.files['file_give']
    # gridfs 활용해서 이미지 분할 저장
    fs_image_id = fs.put(file)
    # db 추가
    doc = {
        'title': title_receive,
        'img': fs_image_id
    }
    db.mlimage.insert_one(doc)
    return jsonify({'result':'사진 저장 완료'})

@app.route('/2page/<title>')
def two_page_img(title):
    # title은 현재 이미지타이틀이므로, 그것을 이용해서 db에서 이미지 '파일'을 가지고 옴
    img_info = db.mlimage.find_one({'title': title})
    image = img_decode(img_info['img'])
    # 해당 이미지의 데이터를 jinja 형식으로 사용하기 위해 넘김
    return render_template("2page_img.html", img=image)

def img_decode(image):
    img_binary = fs.get(image)
    base64_data = codecs.encode(img_binary.read(), 'base64')
    # html 파일로 넘겨줄 수 있도록, base64 형태의 데이터로 변환
    image_decoded = base64_data.decode('utf-8')
    return image_decoded

## 3페이지 ################################################################################################################################

@app.route('/3page/')
def three_page():
    return render_template("3page.html")

## 4페이지 ################################################################################################################################

@app.route('/4page/')
def four_page():
    return render_template("4page.html")

## 끝 ################################################################################################################################

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)