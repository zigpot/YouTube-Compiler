import os
import sys

def srt_to_txt_DEPRECATED(srt_path):
    with open(srt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    text = ' '.join(
        line.strip() for line in lines
        if line.strip() and not line.strip().isdigit() and '-->' not in line
    )
    txt_path = srt_path.rsplit('.', 1)[0] + '.txt'
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Converted: {srt_path} → {txt_path}")

def srt_to_txt(srt_file):
    with open(srt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    text = ' '.join(
        line.strip() for line in lines
        if not line.strip().isdigit() and '-->' not in line and line.strip()
    )
    
    # Remove '.en.srt' or just '.srt'
    base_name = os.path.basename(srt_file)
    if base_name.endswith('.en.srt'):
        new_name = base_name.replace('.en.srt', '.txt')
    else:
        new_name = base_name.replace('.srt', '.txt')
    
    txt_file = os.path.join(os.path.dirname(srt_file), new_name)
    
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(text)

    os.remove(srt_file)  # delete original .srt

def convert_all_srt_in_dir(directory='.'):
    for filename in os.listdir(directory):
        if filename.endswith('.srt'):
            srt_to_txt(os.path.join(directory, filename))

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python script.py <input_directory> [output_directory]")
        sys.exit(1)
    convert_all_srt_in_dir(sys.argv[1])


