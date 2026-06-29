#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) == 4:
        movie_id = fields[1]
        rating = float(fields[2])
        if rating > 4.0:  # 只筛选高分评价
            print(f"{movie_id}\t1")
