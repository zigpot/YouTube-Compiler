# YouTube Caption Processor

A pipeline to fetch, clean, and compile automated English captions from YouTube videos into a single formatted Word document.

here's the pipeline:

1. Get video automated (English) captions CCs. Run:
```python get_videos.py```
Make sure `list` exists with URL on each line.
2. Convert srt to txt run with:
```python convert_srt_to_txt.py```
3. Add punctuation by
```python punctuate.py```
4. Fix capitalization:
```capitalize.py```
5. compile all files:
```compile_to_docx.py```
