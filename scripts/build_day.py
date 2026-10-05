"""Run the whole pipeline for one day:  python build_day.py N [--engine espeak|edge|piper]"""
import sys
import time

import captions, visuals, tts, assemble, qc
from common import *


def build(day, engine=None):
    t0 = time.time()
    tts.build(day, engine)
    visuals.build(day)
    captions.build(day)
    assemble.build(day)
    res = qc.run_qc(day)
    print(f"day {day:02d} done in {time.time() - t0:.0f}s")
    return res


if __name__ == "__main__":
    eng = sys.argv[sys.argv.index("--engine") + 1] if "--engine" in sys.argv else None
    build(int(sys.argv[1]), eng)
