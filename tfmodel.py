import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input

MODEL_PATH = 'static/model/pokemon_mobilenetv2_model.h5'
model = load_model(MODEL_PATH)

print('Model loaded. Start serving...')


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


#테스트 시 사용했던 클래스라벨
test_class_indices = {'Abra': 0, 'Aerodactyl': 1, 'Alakazam': 2, 'Alolan Sandslash': 3, 'Arbok': 4, 'Arcanine': 5, 'Articuno': 6, 'Beedrill': 7, 'Bellsprout': 8, 'Blastoise': 9, 'Bulbasaur': 10, 'Butterfree': 11, 'Caterpie': 12, 'Chansey': 13, 'Charizard': 14, 'Charmander': 15, 'Charmeleon': 16, 'Clefable': 17, 'Clefairy': 18, 'Cloyster': 19, 'Cubone': 20, 'Dewgong': 21, 'Diglett': 22, 'Ditto': 23, 'Dodrio': 24, 'Doduo': 25, 'Dragonair': 26, 'Dragonite': 27, 'Dratini': 28, 'Drowzee': 29, 'Dugtrio': 30, 'Eevee': 31, 'Ekans': 32, 'Electabuzz': 33, 'Electrode': 34, 'Exeggcute': 35, 'Exeggutor': 36, 'Farfetchd': 37, 'Fearow': 38, 'Flareon': 39, 'Gastly': 40, 'Gengar': 41, 'Geodude': 42, 'Gloom': 43, 'Golbat': 44, 'Goldeen': 45, 'Golduck': 46, 'Golem': 47, 'Graveler': 48, 'Grimer': 49, 'Growlithe': 50, 'Gyarados': 51, 'Haunter': 52, 'Hitmonchan': 53, 'Hitmonlee': 54, 'Horsea': 55, 'Hypno': 56, 'Ivysaur': 57, 'Jigglypuff': 58, 'Jolteon': 59, 'Jynx': 60, 'Kabuto': 61, 'Kabutops': 62, 'Kadabra': 63, 'Kakuna': 64, 'Kangaskhan': 65, 'Kingler': 66, 'Koffing': 67, 'Krabby': 68, 'Lapras': 69, 'Lickitung': 70, 'Machamp': 71, 'Machoke': 72, 'Machop': 73, 'Magikarp': 74, 'Magmar': 75, 'Magnemite': 76, 'Magneton': 77, 'Mankey': 78, 'Marowak': 79, 'Meowth': 80, 'Metapod': 81, 'Mew': 82, 'Mewtwo': 83, 'Moltres': 84, 'MrMime': 85, 'Muk': 86, 'Nidoking': 87, 'Nidoqueen': 88, 'Nidorina': 89, 'Nidorino': 90, 'Ninetales': 91, 'Oddish': 92, 'Omanyte': 93, 'Omastar': 94, 'Onix': 95, 'Paras': 96, 'Parasect': 97, 'Persian': 98, 'Pidgeot': 99, 'Pidgeotto': 100, 'Pidgey': 101, 'Pikachu': 102, 'Pinsir': 103, 'Poliwag': 104, 'Poliwhirl': 105, 'Poliwrath': 106, 'Ponyta': 107, 'Porygon': 108, 'Primeape': 109, 'Psyduck': 110, 'Raichu': 111, 'Rapidash': 112, 'Raticate': 113, 'Rattata': 114, 'Rhydon': 115, 'Rhyhorn': 116, 'Sandshrew': 117, 'Sandslash': 118, 'Scyther': 119, 'Seadra': 120, 'Seaking': 121, 'Seel': 122, 'Shellder': 123, 'Slowbro': 124, 'Slowpoke': 125, 'Snorlax': 126, 'Spearow': 127, 'Squirtle': 128, 'Starmie': 129, 'Staryu': 130, 'Tangela': 131, 'Tauros': 132, 'Tentacool': 133, 'Tentacruel': 134, 'Vaporeon': 135, 'Venomoth': 136, 'Venonat': 137, 'Venusaur': 138, 'Victreebel': 139, 'Vileplume': 140, 'Voltorb': 141, 'Vulpix': 142, 'Wartortle': 143, 'Weedle': 144, 'Weepinbell': 145, 'Weezing': 146, 'Wigglytuff': 147, 'Zapdos': 148, 'Zubat': 149}
#클래스 라벨의 키와 밸류 반대로
classes = dict((v, k) for k, v in test_class_indices.items())


img = load_img('static/img/파이리.jfif')
#만든 함수를 사용해서 예측
preds = model_predict(img, model)
#예측결과 나온 확률(최대값)
pred_proba = "{:.3f}".format(np.amax(preds))   
#예측결과의 클래스
pred_label = classes[np.argmax(preds)]
#예측결과 클래스와 확률 출력
print(pred_label, pred_proba)




def top_prob(array):
    ind = np.argpartition(array, -3)[0][-3:]
    ind = ind[np.argsort(array[0][ind])][::-1]
    return array[0][ind]

def top_label(array):
    ind = np.argpartition(array, -3)[0][-3:]
    ind = ind[np.argsort(array[0][ind])][::-1]
    return ind


img2 = load_img('static/img/파이리.jfif')
#만든 함수를 사용해서 예측
preds2 = model_predict(img2, model)
#예측결과 나온 확률(최대값)
# pred_proba2 = "{:.3f}".format(top_prob(preds2))   
#예측결과의 클래스
# pred_label2 = classes[top_label(preds2)]
#예측결과 클래스와 확률 출력
print(top_label(preds2), top_prob(preds2))

result_dict = {}
for i in range(3):
    result_dict[classes[top_label(preds2)[i]]] = round(top_prob(preds2)[i], 4)
print(result_dict)
