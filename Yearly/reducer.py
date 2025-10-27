#!/usr/bin/env python3
import sys

current_year = None
total = 0.0
count = 0

# Print CSV header
print("year,avg_wat_basal_t")

for line in sys.stdin:
    try:
        year, value = line.strip().split(',')
        value = float(value)
    except:
        continue

    if current_year == year:
        total += value
        count += 1
    else:
        if current_year:
            avg = total / count
            print(f"{current_year},{avg:.2f}")
        current_year = year
        total = value
        count = 1

# Final output
if current_year:
    avg = total / count
    print(f"{current_year},{avg:.2f}")
