#!/usr/bin/env python3
import sys

current_genre = None
total_sum = 0
total_count = 0

for line in sys.stdin:
    genre, rating, count = line.strip().split('\t')
    rating = float(rating)
    count = int(count)
    
    if current_genre == genre:
        total_sum += rating
        total_count += count
    else:
        if current_genre:
            avg = total_sum / total_count
            print(f"{current_genre}\t{avg}\t{total_count}")
        current_genre = genre
        total_sum = rating
        total_count = count

if current_genre:
    avg = total_sum / total_count
    print(f"{current_genre}\t{avg}\t{total_count}")
