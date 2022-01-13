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

from datetime import datetime


MODEL_PATH = 'static/model/pokemon_ResNet50V2_03_model.h5'
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
    test_class_indices = {'Abra': 0, 'Aerodactyl': 1, 'Alakazam': 2, 'Alolan Sandslash': 3, 'Arbok': 4, 'Arcanine': 5, 'Articuno': 6, 'Beedrill': 7, 'Bellsprout': 8, 'Blastoise': 9, 'Bulbasaur': 10, 'Butterfree': 11, 'Caterpie': 12, 'Chansey': 13, 'Charizard': 14, 'Charmander': 15, 'Charmeleon': 16, 'Clefable': 17, 'Clefairy': 18, 'Cloyster': 19, 'Cubone': 20, 'Dewgong': 21, 'Diglett': 22, 'Ditto': 23, 'Dodrio': 24, 'Doduo': 25, 'Dragonair': 26, 'Dragonite': 27, 'Dratini': 28, 'Drowzee': 29, 'Dugtrio': 30, 'Eevee': 31, 'Ekans': 32, 'Electabuzz': 33, 'Electrode': 34, 'Exeggcute': 35, 'Exeggutor': 36, 'Farfetchd': 37, 'Fearow': 38, 'Flareon': 39, 'Gastly': 40, 'Gengar': 41, 'Geodude': 42, 'Gloom': 43, 'Golbat': 44, 'Goldeen': 45, 'Golduck': 46, 'Golem': 47, 'Graveler': 48, 'Grimer': 49, 'Growlithe': 50, 'Gyarados': 51, 'Haunter': 52, 'Hitmonchan': 53, 'Hitmonlee': 54, 'Horsea': 55, 'Hypno': 56, 'Ivysaur': 57, 'Jigglypuff': 58, 'Jolteon': 59, 'Jynx': 60, 'Kabuto': 61, 'Kabutops': 62, 'Kadabra': 63, 'Kakuna': 64, 'Kangaskhan': 65, 'Kingler': 66, 'Koffing': 67, 'Krabby': 68, 'Lapras': 69, 'Lickitung': 70, 'Machamp': 71, 'Machoke': 72, 'Machop': 73, 'Magikarp': 74, 'Magmar': 75, 'Magnemite': 76, 'Magneton': 77, 'Mankey': 78, 'Marowak': 79, 'Meowth': 80, 'Metapod': 81, 'Mew': 82, 'Mewtwo': 83, 'Moltres': 84, 'MrMime': 85, 'Muk': 86, 'Nidoking': 87, 'Nidoqueen': 88, 'Nidorina': 89, 'Nidorino': 90, 'Ninetales': 91, 'Oddish': 92, 'Omanyte': 93, 'Omastar': 94, 'Onix': 95, 'Paras': 96, 'Parasect': 97, 'Persian': 98, 'Pidgeot': 99, 'Pidgeotto': 100, 'Pidgey': 101, 'Pikachu': 102, 'Pinsir': 103, 'Poliwag': 104, 'Poliwhirl': 105, 'Poliwrath': 106, 'Ponyta': 107, 'Porygon': 108, 'Primeape': 109, 'Psyduck': 110, 'Raichu': 111, 'Rapidash': 112, 'Raticate': 113, 'Rattata': 114, 'Rhydon': 115, 'Rhyhorn': 116, 'Sandshrew': 117, 'Sandslash': 118, 'Scyther': 119, 'Seadra': 120, 'Seaking': 121, 'Seel': 122, 'Shellder': 123, 'Slowbro': 124, 'Slowpoke': 125, 'Snorlax': 126, 'Spearow': 127, 'Squirtle': 128, 'Starmie': 129, 'Staryu': 130, 'Tangela': 131, 'Tauros': 132, 'Tentacool': 133, 'Tentacruel': 134, 'Vaporeon': 135, 'Venomoth': 136, 'Venonat': 137, 'Venusaur': 138, 'Victreebel': 139, 'Vileplume': 140, 'Voltorb': 141, 'Vulpix': 142, 'Wartortle': 143, 'Weedle': 144, 'Weepinbell': 145, 'Weezing': 146, 'Wigglytuff': 147, 'Zapdos': 148, 'Zubat': 149}
    # 1세대포켓몬 https://www.kaggle.com/thedagger/pokemon-generation-one
    test_class_indices2 = {'Abra': 0, 'Aerodactyl': 1, 'Alakazam': 2, 'Arbok': 3, 'Arcanine': 4, 'Articuno': 5, 'Beedrill': 6, 'Bellsprout': 7, 'Blastoise': 8, 'Bulbasaur': 9, 'Butterfree': 10, 'Caterpie': 11, 'Chansey': 12, 'Charizard': 13, 'Charmander': 14, 'Charmeleon': 15, 'Clefable': 16, 'Clefairy': 17, 'Cloyster': 18, 'Cubone': 19, 'Dewgong': 20, 'Diglett': 21, 'Ditto': 22, 'Dodrio': 23, 'Doduo': 24, 'Dragonair': 25, 'Dragonite': 26, 'Dratini': 27, 'Drowzee': 28, 'Dugtrio': 29, 'Eevee': 30, 'Ekans': 31, 'Electabuzz': 32, 'Electrode': 33, 'Exeggcute': 34, 'Exeggutor': 35, 'Farfetchd': 36, 'Fearow': 37, 'Flareon': 38, 'Gastly': 39, 'Gengar': 40, 'Geodude': 41, 'Gloom': 42, 'Golbat': 43, 'Goldeen': 44, 'Golduck': 45, 'Golem': 46, 'Graveler': 47, 'Grimer': 48, 'Growlithe': 49, 'Gyarados': 50, 'Haunter': 51, 'Hitmonchan': 52, 'Hitmonlee': 53, 'Horsea': 54, 'Hypno': 55, 'Ivysaur': 56, 'Jigglypuff': 57, 'Jolteon': 58, 'Jynx': 59, 'Kabuto': 60, 'Kabutops': 61, 'Kadabra': 62, 'Kakuna': 63, 'Kangaskhan': 64, 'Kingler': 65, 'Koffing': 66, 'Krabby': 67, 'Lapras': 68, 'Lickitung': 69, 'Machamp': 70, 'Machoke': 71, 'Machop': 72, 'Magikarp': 73, 'Magmar': 74, 'Magnemite': 75, 'Magneton': 76, 'Mankey': 77, 'Marowak': 78, 'Meowth': 79, 'Metapod': 80, 'Mew': 81, 'Mewtwo': 82, 'Moltres': 83, 'MrMime': 84, 'Muk': 85, 'Nidoking': 86, 'Nidoqueen': 87, 'Nidorina': 88, 'Nidorino': 89, 'Ninetales': 90, 'Oddish': 91, 'Omanyte': 92, 'Omastar': 93, 'Onix': 94, 'Paras': 95, 'Parasect': 96, 'Persian': 97, 'Pidgeot': 98, 'Pidgeotto': 99, 'Pidgey': 100, 'Pikachu': 101, 'Pinsir': 102, 'Poliwag': 103, 'Poliwhirl': 104, 'Poliwrath': 105, 'Ponyta': 106, 'Porygon': 107, 'Primeape': 108, 'Psyduck': 109, 'Raichu': 110, 'Rapidash': 111, 'Raticate': 112, 'Rattata': 113, 'Rhydon': 114, 'Rhyhorn': 115, 'Sandshrew': 116, 'Sandslash': 117, 'Scyther': 118, 'Seadra': 119, 'Seaking': 120,  'Seel': 121, 'Shellder': 122, 'Slowbro': 123, 'Slowpoke': 124, 'Snorlax': 125, 'Spearow': 126, 'Squirtle': 127, 'Starmie': 128, 'Staryu': 129, 'Tangela': 130, 'Tauros': 131, 'Tentacool': 132, 'Tentacruel': 133, 'Vaporeon': 134, 'Venomoth': 135, 'Venonat': 136, 'Venusaur': 137, 'Victreebel': 138, 'Vileplume': 139, 'Voltorb': 140, 'Vulpix': 141, 'Wartortle': 142, 'Weedle': 143, 'Weepinbell': 144, 'Weezing': 145, 'Wigglytuff': 146, 'Zapdos': 147, 'Zubat': 148, 'dataset': 149}    
    
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
    if pred_label == 'Alolan Sandslash':
        return 'Sandslash'
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
    file = request.files['file_give']
    # 해당 파일에서 확장자명만 추출
    extension = file.filename.split('.')[-1]
    # 파일 이름이 중복되면 안되므로, 지금 시간을 해당 파일 이름으로 만들어서 중복이 되지 않게 함!
    today = datetime.now()
    savetime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{savetime}'
    # 파일 저장 경로 설정 (파일은 db가 아니라, 서버 컴퓨터 자체에 저장됨)
    save_to = f'static/{filename}.{extension}'
    # 파일 저장!
    file.save(save_to)

    img = load_img(save_to)
    #에측모델분석
    predict = pred_result(img)

    # 아래와 같이 입력하면 db에 추가 가능!
    doc = {'img':f'{filename}.{extension}', 'pred':predict}
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