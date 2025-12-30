import sys
import json

with open("kennethian.json", "r", encoding="utf-8") as f:
    DICTIONARY = json.load(f)

def translate(text: str) -> str:
    for swedish, kennethian in DICTIONARY.items():
        if swedish in text:
            return text.replace(swedish, kennethian)
    return f"{text} (Kennethian: oklart, men det känns som ett problem.)"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py \"Din svenska text\"")
        sys.exit(1)

    input_text = sys.argv[1]
    print(translate(input_text))
