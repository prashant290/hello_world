"""Export title/description/hashtags/thumbnail path for a range of days to output/upload_metadata.csv.
Usage: python export_metadata.py [A B]"""
import csv
import sys

from common import *

a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (1, 90)
rows = []
for d in range(a, b + 1):
    if not (day_dir(d) / "script.json").exists():
        continue
    s = load_script(d)
    rows.append({"day": d, "title": s["title"], "description": s["description"] + "\n\n" + " ".join(s["hashtags"]),
                 "hashtags": " ".join(s["hashtags"]), "video": f"output/day_{d:02d}.mp4",
                 "thumbnail": f"output/thumbnails/day_{d:02d}.png", "accuracy_note": s["accuracy_note"]})
with (OUTPUT / "upload_metadata.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(rows[0]))
    w.writeheader(); w.writerows(rows)
print(len(rows), "rows ->", OUTPUT / "upload_metadata.csv")
