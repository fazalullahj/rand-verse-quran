import pyperclip
from PIL import Image, ImageDraw, ImageFont
import os
import random
import requests


def bring_verse(verse):
    url = (
        "http://api.alquran.cloud/ayah/"
        + str(verse)
        + "/editions/quran-uthmani,en.asad"
    )
    json_data = requests.get(url).json()
    verse_a = json_data["data"][0]["text"]
    verse_en = json_data["data"][1]["text"]
    sura = (
        json_data["data"][0]["surah"]["englishName"]
        + "("
        + str(json_data["data"][0]["surah"]["number"])
        + "):"
        + str(json_data["data"][0]["numberInSurah"])
    )
    return [verse_a, verse_en, sura]


def copy_verse_to_clipboard(verse_data):
    
    verse_text = f"{verse_data[0]}\n\n{verse_data[1]}\n\n{verse_data[2]}"

    pyperclip.copy(verse_text)


if __name__ == "__main__":

    random_verse = random.randint(1, 6237)
    verse_data = bring_verse(random_verse)

    copy_verse_to_clipboard(verse_data)

    print("Verse copied to clipboard successfully!")
    print(f"\n{verse_data[0]}\n\n{verse_data[1]}\n\n{verse_data[2]}")
