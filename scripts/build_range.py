"""Build days A..B and print a QC summary:  python build_range.py A B"""
import sys
import traceback

import build_day
from common import *

a, b = int(sys.argv[1]), int(sys.argv[2])
rows = []
for d in range(a, b + 1):
    try:
        r = build_day.build(d)
        rows.append((d, "PASS" if r["passed"] else "FAIL", "; ".join(r["issues"])))
    except Exception as e:                       # keep going; record the failure
        traceback.print_exc()
        tracker_update(d, qc_passed="FALSE", notes=f"build error: {e}"[:300])
        rows.append((d, "ERROR", str(e)[:120]))
print("\n==== summary ====")
for d, s, n in rows:
    print(f"day {d:02d}  {s:5s}  {n}")
print(f"{sum(r[1] == 'PASS' for r in rows)}/{len(rows)} passed")
