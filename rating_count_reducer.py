#!/usr/bin/env python3
import sys

current_movie = None
current_count = 0

for line in sys.stdin:
    movie_id, count = line.strip().split('\t')
    count = int(count)
    
    if current_movie == movie_id:
        current_count += count
    else:
        if current_movie:
            print(f"{current_movie}\t{current_count}")
        current_movie = movie_id
        current_count = count

# 输出最后一个电影
if current_movie:
    print(f"{current_movie}\t{current_count}")
