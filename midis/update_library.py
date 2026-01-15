import os
import json

# Settings
REPO_NAME = "Jade-Lyre-Library"
USERNAME = "JadeLyre"
MIDI_FOLDER = "midis"
JSON_FILE = "library.json"

def generate_library():
    library = []
    if not os.path.exists(MIDI_FOLDER):
        os.makedirs(MIDI_FOLDER)

    for idx, filename in enumerate(os.listdir(MIDI_FOLDER)):
        if filename.endswith(".mid") or filename.endswith(".midi"):
            # Clean up the name for the UI
            clean_name = filename.replace(".mid", "").replace(".midi", "").replace("_", " ").title()
            
            # Smart Categorization
            category = "Wuxia" if "jade" in clean_name.lower() or "zen" in clean_name.lower() else "Pop"
            
            entry = {
                "id": idx + 1,
                "title": clean_name,
                "author": "Community",
                "category": category,
                "url": f"https://raw.githubusercontent.com/{USERNAME}/{REPO_NAME}/main/{MIDI_FOLDER}/{filename}"
            }
            library.append(entry)

    with open(JSON_FILE, "w") as f:
        json.dump(library, f, indent=2)

if __name__ == "__main__":
    generate_library()
