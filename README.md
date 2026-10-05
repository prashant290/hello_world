# The Psyche Discourse — Shorts pipeline
90 psychology Shorts (50 s, 1080x1920, 30 fps). Voice: Kokoro `am_michael` (free, offline). Look: hand-drawn stickman, sage/navy/orange.

## One-time setup (Mac/Linux)
1. Install ffmpeg (`brew install ffmpeg`) and Python 3.10+.
2. `pip install pillow numpy soundfile kokoro-onnx`
3. Download the two voice files into `assets/voices/` (≈350 MB, free):
   https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
   https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
4. `cd scripts && python make_music.py`   (generates royalty-free background music)

## Use
- `python scripts/write_scripts.py`  builds/validates script.json from scripts/content/batch_*.py
- `python scripts/build_day.py 1`    builds output/day_01.mp4 and runs QC
- `python scripts/build_range.py 2 8` builds a week
Status lives in `tracker.csv`; settings (voice, colors, schedule) in `config.json`.
