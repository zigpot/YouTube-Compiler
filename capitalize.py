import os
import re
import sys

def capitalize_sentences(text):
    def cap(match):
        return match.group(1) + match.group(2).upper()
    return re.sub(r'(^|[.?!]\s+)([a-z])', cap, text.strip())

if len(sys.argv) < 2:
    print("Usage: python script.py <input_directory> <output_dir_optional>")
    sys.exit(1)

input_dir = sys.argv[1]  # replace with your folder path

if len(sys.argv) < 2:
    output_dir = "./capitalized"    # output folder
else:
    output_dir = sys.argv[2] +"/capitalized"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"{filename}")

        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        capitalized = capitalize_sentences(text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(capitalized)

