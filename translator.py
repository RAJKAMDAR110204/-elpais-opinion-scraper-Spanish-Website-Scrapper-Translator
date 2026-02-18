import requests
import os

RAPIDAPI_KEY = "6284c4e921msh467e184af57e789p197e72jsn53631ecbd0d7"


URL = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
}


def translate_title(title):
    if not title:
        return ""

    payload = {
        "from": "es",
        "to": "en",
        "text": title
    }

    response = requests.post(URL, json=payload, headers=HEADERS)

    if response.status_code == 200:
        translated_text = response.json()["trans"]
        print("Translated Title:", translated_text)
        return translated_text
    else:
        print("Translation error:", response.text)
        return ""
