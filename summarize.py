#!/usr/bin/env python3
"""Sum unbilled hours and amounts per client from a CSV time log (AI-agent made, MIT)."""
import csv, sys, collections
t = collections.defaultdict(lambda: [0.0, 0.0])
for r in csv.DictReader(open(sys.argv[1])):
    if r["billed"].strip().lower() != "yes":
        h = float(r["hours"]); t[r["client"]][0] += h; t[r["client"]][1] += h * float(r["rate_usd"])
for c, (h, a) in t.items():
    print(f"{c}: {h:.2f} h, ${a:.2f} unbilled")
