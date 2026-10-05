# The Psyche Discourse

Faceless YouTube Shorts channel: 90 research-backed everyday-psychology Shorts. Read `CLAUDE.md` first (rules, folder map, current state).

- `plan/` — topic review of the 90 ideas, content plan, calendar, tracker
- `scripts_and_sources/` — each day's script + per-sentence source table (`sources.md`)
- `videos/` — finished MP4s and thumbnails (MP4s are not in git)
- `channel_kit/` — brand, config, logo, fonts, upload sheet
- `src/` — the local renderer (Python + ffmpeg, free tools only)

Setup (one time): install ffmpeg + Python 3.10+; `pip install pillow numpy soundfile kokoro-onnx pocketsphinx`;
download the two free Kokoro voice files listed in `channel_kit/config.json` (`tts.kokoro._download`) into `channel_kit/voices/`;
run `python src/make_music.py`. Build: `python src/build_day.py 1`, `python src/build_range.py 1 7`, review: `python src/review.py 1`.
