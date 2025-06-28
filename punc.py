import os
import sys
from deepmultilingualpunctuation import PunctuationModel

# Initialize model once
model = PunctuationModel()

# Directory containing .txt files
if len(sys.argv) < 2:
    print("Usage: python script.py <input_directory> <output_dir_optional>")
    sys.exit(1)

input_dir = sys.argv[1]

for filename in os.listdir(input_dir):
    print(filename)
# Loop through all .txt files
for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_dir, filename)
        print(f"Punctuating: {filename}...")

        # Read original text
        with open(input_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        # Apply punctuation restoration
        restored = model.restore_punctuation(raw_text)

        # Write output
        output_filename = filename
        output_dir =  os.path.join(input_dir, "punctuated")
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(restored)

        print(f"Punctuated: {filename} → {output_filename}")

