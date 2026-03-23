import random
import requests

BASE_URL = "https://bhagavad-gita3.p.rapidapi.com/v2/chapters"

HEADERS = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "bhagavad-gita3.p.rapidapi.com",
    "x-rapidapi-key": "fb0fdad3b8mshf47b51fd57ae795p1fb6aajsn3ef01fd28e2e"  # 🔴 Replace this
}

# ✅ Chapter → Verse count mapping
CHAPTER_VERSES = {
    1: 47, 2: 72, 3: 43, 4: 42, 5: 29, 6: 47,
    7: 30, 8: 28, 9: 34, 10: 42, 11: 55, 12: 20,
    13: 35, 14: 27, 15: 20, 16: 24, 17: 28, 18: 78
}

def get_random_shloka():
    chapter = random.randint(1, 18)
    verse = random.randint(1, CHAPTER_VERSES[chapter])

    url = f"{BASE_URL}/{chapter}/verses/{verse}/"

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")

        data = response.json()

        return {
            "chapter": chapter,
            "verse": verse,
            "text": data.get("text", "No shloka found"),
            "transliteration": data.get("transliteration", ""),
            "translation": data.get("translations", [{}])[0].get("description", "")
        }

    except Exception as e:
        print("Error fetching shloka:", e)

        return {
            "chapter": chapter,
            "verse": verse,
            "text": "Unable to fetch shloka",
            "transliteration": "",
            "translation": ""
        }
    