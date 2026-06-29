#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) == 4:  # u.data格式：user_id, movie_id, rating, timestamp
        movie_id = fields[1]  # 第2列是movie_id
        print(f"{movie_id}\t1")
