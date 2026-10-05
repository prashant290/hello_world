"""Step 1: create /shorts/day_01..day_90, /assets, /scripts, /output and tracker.csv."""
from common import *

topics = load_topics()
assert len(topics) == 90, f"expected 90 topics, found {len(topics)}"
for d in range(1, 91):
    day_dir(d).mkdir(parents=True, exist_ok=True)
for p in (ASSETS, OUTPUT):
    p.mkdir(exist_ok=True)
tracker_init(topics)
print("project ready:", len(topics), "topics")
