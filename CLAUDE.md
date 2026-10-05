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
- Look: hand-drawn stickman + 3-frame boil, palette from `channel_kit/config.json` (sage bg, navy ink, orange accent). Logo = the owner's real mark (`channel_kit/logo.png`, supplied 2026-10-05; the old recreation is `logo_recreated_old.png`, made by `src/make_logo.py`).
- Git: push to branch `claude/youtube-shorts-psychology-fq5fjx` (GitHub access works via `git push`; if 403, `add_repo` with access=push then retry).
- No YouTube upload from the sandbox (needs the owner's Google credentials + network). Upload is manual or an optional script only if the owner confirms.

## CURRENT STATE (update me)
- **Done (2026-10-05):** folder structure; topic review of all 90 ideas (`plan/topic_review.md`: 37 kept / 47 reframed / 6 replaced; final list `plan/topics_final.csv`);
  content plan + calendar (Day 1 = Tue 6 Oct 2026, editable); sourcing/validation tooling; **Days 1-30 scripted, built, QC'd (30/30 pass) and self-reviewed**
  (frames of every video inspected; audio transcribed offline and matched to the script, similarity 0.60-0.81; durations 49.0-49.5 s; peaks <= -1.6 dB; voice 18+ dB over music).
  Titles/descriptions/hashtags/thumbnails for Days 1-30: `channel_kit/upload_metadata.csv`, `videos/thumbnails/`.
- **Not started:** scripts for Days 31-90. Topics are fixed in `plan/topics_final.csv`; sources named in `plan/topic_review.md` must be re-verified per sentence (web search) when scripting. Month 2 starts with Day 31 (mimicry: Chartrand & Bargh 1999; Maddux et al. 2008).
- **Needs the owner:** (a) posting time + timezone, (b) —(logo received and applied), (c) YouTube upload is manual or needs their OK + Google credentials (not possible from the sandbox).
- **Known limits:** voice is Kokoro am_michael (good, not human); word timings come from audio energy (no ASR); sources were checked through web-search summaries of abstracts/publisher pages (each source's `verified` note says which; a few figures rest on secondary summaries and are flagged in that day's caveats); the offline recognizer used for audio checks is weak (similarity 0.6+ means the right words are spoken).
- **Lessons learned (apply to Days 31-90):**
  1. Titles, thumbnails, descriptions and on-screen text are claims too — hedge contested ones, prefer questions. Never claim what stores/marketers do without a source.
  2. Charts must match their sentence: use `bars:label=hNN` (height only) when the source gives no number; never invent figures.
  3. Check the audio under every caption chunk (QC does) and LOOK at frames: QC cannot see misleading visuals or overlapping art.
  4. Re-verify numbers from memory (Liikkanen: 89.2% not 91.7%; doorway-effect "go back to the room" advice was wrong; Zeigarnik effect failed to replicate).
  5. Don't `pkill -f` a pattern that appears in your own command line; don't commit `channel_kit/voices/*.onnx|bin` (ignored).
