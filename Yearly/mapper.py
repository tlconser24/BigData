#!/usr/bin/env python3
import sys
import csv

reader = csv.DictReader(sys.stdin)
for row in reader:
    try:
        year = row['year']
        wat_basal_t = float(row['wat_basal_t'])
        if wat_basal_t >= 0:
            print(f"{year},{wat_basal_t}")
    except:
        continue
