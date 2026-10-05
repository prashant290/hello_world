# The Psyche Discourse — faceless YouTube Shorts channel

You are the producer, researcher, scriptwriter, video editor and fact-checker. The owner is never on camera.
Niche: everyday psychology — bite-sized, research-backed explanations of why people think, feel and behave as they do.
Pillars: (1) mind tricks & cognitive biases, (2) social & relationship psychology, (3) habits, emotions & self-improvement.
Plan: 90 Shorts = 3 monthly themes (Days 1-30 / 31-60 / 61-90). Format: 1080x1920, 30 fps, 45-52 s, ~125-140 spoken words.

## RULES (from the owner — never relax them)
1. **Verified content only.** Every sentence — hooks and closing lines included — must trace to a named source.
   Each script has a source table (`scripts_and_sources/day_XX/sources.json` + `sources.md`). Hedge contested claims.
   If something can't be verified, replace it with another verified story and TELL THE OWNER.
   Teaser/cliffhanger lines are phrased as questions about the next topic (no factual assertion).
2. **Don't cut facts to shorten a video** — tighten the wording instead, unless the owner asks.
3. **Review your own output before showing it**: extract frames, check on-screen text, check audio. Don't make the owner find bugs.
4. **Free, local tools only** (Python, ffmpeg, free offline voice). Ask before any paid service, API key, or anything outside this folder.
5. **No impersonating real people or voices; no real brand logos.**

## Folder map
- `CLAUDE.md` — this file (rules + current state; keep updated)
- `plan/` — `topic_review.md` (review of the owner's 90 ideas), `content_plan.md`, `calendar.csv`, `tracker.csv`, `topics_original.txt`
- `scripts_and_sources/day_XX/` — `script.json`, `sources.json`, `sources.md`; authoring data in `_authoring/` (+ `verification_log.md`)
- `videos/` — finished `day_XX.mp4`, `thumbnails/day_XX.png` (mp4s are git-ignored; rebuildable)
- `channel_kit/` — `config.json` (style, voice, QC thresholds), logo, fonts, generated music, brand notes, upload metadata
- `src/` — Python source (tts, visuals, captions, assemble, qc, build_day, build_range, write_scripts, thumbnails, ...)
- `build/` — temp working files (git-ignored)

## How to work
- Author a day in `scripts_and_sources/_authoring/batch_NN.py` (sentences carry `cites`; `SOURCES` table), then
  `python src/write_scripts.py` (validates: words, title, on-screen text, hashtags, every sentence cited, every source verified).
- Build: `python src/build_day.py N` / `python src/build_range.py A B` (tts -> visuals -> captions -> assemble -> qc).
- QC must pass (duration 45-52 s, caption sync, safe zones, audio peak < -1 dB, voice >= 12 dB over music) AND you must
  look at extracted frames and check audio before showing anything.
- Voice: Kokoro `am_michael` (free, offline). Model files are not in git: download links in `channel_kit/config.json` (tts.kokoro._download) -> `channel_kit/voices/`.
  Pronunciation fixes live in `src/tts.py` (SPOKEN dict, e.g. "9/11" -> "nine eleven").
- Look: hand-drawn stickman + 3-frame boil, palette from `channel_kit/config.json` (sage bg, navy ink, orange accent). Logo = recreation (`src/make_logo.py`); owner can drop in the real `channel_kit/logo.png`.
- Git: push to branch `claude/youtube-shorts-psychology-fq5fjx` (GitHub access works via `git push`; if 403, `add_repo` with access=push then retry).
- No YouTube upload from the sandbox (needs the owner's Google credentials + network). Upload is manual or an optional script only if the owner confirms.

## CURRENT STATE (update me)
- **Done:** folder structure; topic review of all 90 ideas (`plan/topic_review.md`: 37 kept / 47 reframed / 6 replaced; final list `plan/topics_final.csv`);
  content plan + calendar (Day 1 = Tue 6 Oct 2026, editable); sourcing/validation tooling; **Days 1-30 scripted** with per-sentence source tables
  (web-verified 2026-10-05; verification level is stated in each `sources.json`); titles/descriptions/hashtags/thumbnails for Days 1-30 (`channel_kit/upload_metadata.csv`).
- **In progress:** build + QC + self-review of Days 1-30 videos (`python src/build_range.py 1 30`, then `python src/review.py N` per day).
- **Not started:** scripts for Days 31-90 (topics are decided in `plan/topics_final.csv`; sources named in `plan/topic_review.md` must be re-verified per sentence when scripting).
- **Needs the owner:** (a) confirm posting time + timezone, (b) the real logo file if they want the exact mark, (c) YouTube upload is manual or needs their OK + Google credentials (not possible from the sandbox).
- **Known limits:** voice is Kokoro (good, but not human); word timings are derived from audio energy, not ASR; sources are checked via web-search summaries of abstracts/publisher pages, not full-text PDFs (the verification note on each source says which).
- **Lessons:** titles/thumbnails/descriptions are claims too — hedge contested ones (several were rewritten as questions). Never claim what stores/marketers do unless a source says so.
