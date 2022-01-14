from flask import Flask, json, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://tester:sparta@cluster0.hntfy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

## imageprocessing ######################################################################################################################

import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input


MODEL_PATH = 'static/model/pokemon_ResNet50V2_04_model.h5'
model = load_model(MODEL_PATH)

print('Model loaded. Start serving...')

## tensorflow predict function ########################################################################################################################################

def model_predict(img, model):
    #테스트시 사용했던 사이즈로 리사이즈
    img = img.resize((224, 224))
    # 이미지의 Preprocessing (참고 : https://github.com/imfing/keras-flask-deploy-webapp)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='tf')
    #예측
    preds = model.predict(x)
    return preds

def pred_result(image):
    #테스트 시 사용했던 클래스라벨
    # 7000라벨 포켓몬 https://www.kaggle.com/lantian773030/pokemonclassification
    test_class_indices = {'Abra': 0, 
    'Aerodactyl': 1,
    'Alakazam': 2,
    'Arbok': 3,
    'Arcanine': 4,
    'Articuno': 5,
    'Beedrill': 6,
    'Bellsprout': 7,
    'Blastoise': 8,
    'Bulbasaur': 9,
    'Butterfree': 10,
    'Caterpie': 11,
    'Chansey': 12,
    'Charizard': 13,
    'Charmander': 14,
    'Charmeleon': 15,
    'Clefable': 16,
    'Clefairy': 17,
    'Cloyster': 18,
    'Cubone': 19,
    'Dewgong': 20,
    'Diglett': 21,
    'Ditto': 22,
    'Dodrio': 23,
    'Doduo': 24,
    'Dragonair': 25,
    'Dragonite': 26,
    'Dratini': 27,
    'Drowzee': 28,
    'Dugtrio': 29,
    'Eevee': 30,
    'Ekans': 31,
    'Electabuzz': 32,
    'Electrode': 33,
    'Exeggcute': 34,
    'Exeggutor': 35,
    'Farfetchd': 36,
    'Fearow': 37,
    'Flareon': 38,
    'Gastly': 39,
    'Gengar': 40,
    'Geodude': 41,
    'Gloom': 42,
    'Golbat': 43,
    'Goldeen': 44,
    'Golduck': 45,
    'Graveler': 46,
    'Grimer': 47,
    'Growlithe': 48,
    'Gyarados': 49,
    'Haunter': 50,
    'Hitmonchan': 51,
    'Hitmonlee': 52,
    'Horsea': 53,
    'Hypno': 54,
    'Ivysaur': 55,
    'Jigglypuff': 56,
    'Jolteon': 57,
    'Jynx': 58,
    'Kabutops': 59,
    'Kadabra': 60,
    'Kakuna': 61,
    'Kangaskhan': 62,
    'Kingler': 63,
    'Koffing': 64,
    'Lapras': 65,
    'Lickitung': 66,
    'Machamp': 67,
    'Machoke': 68,
    'Machop': 69,
    'Magikarp': 70,
    'Magmar': 71,
    'Magnemite': 72,
    'Magneton': 73,
    'Mankey': 74,
    'Marowak': 75,
    'Meowth': 76,
    'Metapod': 77,
    'Mew': 78,
    'Mewtwo': 79,
    'Moltres': 80,
    'Mr. Mime': 81,
    'MrMime': 82,
    'Nidoking': 83,
    'Nidoqueen': 84,
    'Nidorina': 85,
    'Nidorino': 86,
    'Ninetales': 87,
    'Oddish': 88,
    'Omanyte': 89,
    'Omastar': 90,
    'Parasect': 91,
    'Pidgeot': 92,
    'Pidgeotto': 93,
    'Pidgey': 94,
    'Pikachu': 95,
    'Pinsir': 96,
    'Poliwag': 97,
    'Poliwhirl': 98,
    'Poliwrath': 99,
    'Ponyta': 100,
    'Porygon': 101,
    'Primeape': 102,
    'Psyduck': 103,
    'Raichu': 104,
    'Rapidash': 105,
    'Raticate': 106,
    'Rattata': 107,
    'Rhydon': 108,
    'Rhyhorn': 109,
    'Sandshrew': 110,
    'Sandslash': 111,
    'Scyther': 112,
    'Seadra': 113,
    'Seaking': 114,
    'Seel': 115,
    'Shellder': 116,
    'Slowbro': 117,
    'Slowpoke': 118,
    'Snorlax': 119,
    'Spearow': 120,
    'Squirtle': 121,
    'Starmie': 122,
    'Staryu': 123,
    'Tangela': 124,
    'Tauros': 125,
    'Tentacool': 126,
    'Tentacruel': 127,
    'Vaporeon': 128,
    'Venomoth': 129,
    'Venonat': 130,
    'Venusaur': 131,
    'Victreebel': 132,
    'Vileplume': 133,
    'Voltorb': 134,
    'Vulpix': 135,
    'Wartortle': 136,
    'Weedle': 137,
    'Weepinbell': 138,
    'Weezing': 139,
    'Wigglytuff': 140,
    'Zapdos': 141,
    'Zubat': 142}
    # 1세대포켓몬 https://www.kaggle.com/thedagger/pokemon-generation-one
    # 1세대포켓몬 https://www.kaggle.com/mikoajkolman/pokemon-images-first-generation17000-files
    
    
    #클래스 라벨의 키와 밸류 반대로
    classes = dict((v, k) for k, v in test_class_indices.items())
    img = image
    #만든 함수를 사용해서 예측
    preds = model_predict(img, model)
    #예측결과 나온 확률(최대값)
    pred_proba = "{:.3f}".format(np.amax(preds))   
    #예측결과의 클래스
    pred_label = classes[np.argmax(preds)]
    #예측결과 클래스와 확률 출력
    print(pred_label, pred_proba)
    
    return pred_label


## 인덱스 페이지 ################################################################################################################################

@app.route('/')
def main():
    return render_template("index.html")


## 업로드 페이지 ################################################################################################################################

@app.route('/upload/')
def upload_page():
    return render_template("upload.html")

@app.route('/api/upload/', methods=['POST'])
def upload_pic():
    # 클라이언트로부터 정보받아옴
    title = request.form['title_give']
    file = request.files['file_give']
    # 해당 파일에서 확장자명만 추출
    extension = file.filename.split('.')[-1]
    # 파일 이름이 중복되면 안되므로, 지금 시간을 해당 파일 이름으로 만들어서 중복이 되지 않게 함!
    savetime = str(title)
    filename = f'{savetime}'
    # 파일 저장 경로 설정 (파일은 db가 아니라, 서버 컴퓨터 자체에 저장됨)
    save_to = f'static/{filename}.{extension}'
    # 파일 저장!
    file.save(save_to)

    img = load_img(save_to)
    #에측모델분석
    predict = pred_result(img)

    # 아래와 같이 입력하면 db에 추가 가능!
    doc = {'title': savetime , 'img':f'{filename}.{extension}', 'pred':predict}
    db.mlimage2.insert_one(doc)

    return jsonify({'msg':'사진 분석 완료!'})

## 결과 페이지 ################################################################################################################################

@app.route('/pokedex/')
def three_page():
    # DB에서 받아올 것.
    return render_template("pokedex.html") #DB받아서 렌더템플릿할때 같이보내줄것


@app.route('/pokedex/<title>')
def result_page(title):
    # DB에서 받아올 것.
    # 이미지 정보
    img_info = db.mlimage2.find_one({'title': title})
    # 이미지 예측결과와 이름이 일치하는 포켓몬 정보
    en = img_info['pred']
    poke_info = db.pokemon.find_one({'eng_name': en})
    #DB받아서 렌더템플릿할때 같이보내줄것
    return render_template("pokedex.html", img_info = img_info, poke_info = poke_info) 

## 끝 ################################################################################################################################

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)