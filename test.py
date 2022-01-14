import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://tester:sparta@cluster0.hntfy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = client.dbsparta

for i in range(1, 152):
    num = f"{i}".zfill(4)
    url = f"https://podic.kr/Gen1/mon/mon{num}.html"
    # print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, "lxml")

    # 포켓몬 인덱스
    index = i

    # 포켓몬 한글 이름
    kor_name = soup.select_one("body > div > p:nth-child(4) > font").text

    # 포켓몬 영어 이름
    names = soup.select_one("body > div > p:nth-child(4)").text
    eng_name = re.sub("[^a-zA-Z]", "", names)

    # 포켓몬 타입 1
    type_1 = soup.select_one(
        "body > div > p:nth-child(6) > span:nth-child(1) > font"
    ).text.strip()

    # 포켓몬 타입 2
    type_2 = soup.select_one("body > div > p:nth-child(6) > span:nth-child(2) > font")
    if type_2:
        type_2 = type_2.text.strip()

    # img
    img = soup.select_one("body > div:nth-child(32) > img")["src"]

    # class
    poke_class = soup.select_one("body > div:nth-child(32) > p:nth-child(5)").text

    # desc
    desc = (
        soup.select_one("#explain > table")
        .text.split("그린")[0]
        .strip()
        .replace("레드", "")
        .strip()
    )

    dict = {
        "index": index,
        "kor_name": kor_name,
        "eng_name": eng_name,
        "type_1": type_1,
        "type_2": type_2,
        "img": img,
        "poke_class": poke_class,
        "desc": desc,
    }
    db.pokemon.insert_one(dict)
# 다됬다.
