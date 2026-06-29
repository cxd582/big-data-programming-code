#!/usr/bin/env python3
import sys

# 预先加载电影类型映射（通过文件读入）
movie_genres = {}
with open('u.item', encoding='latin-1') as f:
    for line in f:
        fields = line.strip().split('|')
        movie_id = fields[0]
        # 类型标签从第5列开始（0/1标记），共19个类型
        genres = []
        genre_names = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 
                       'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 
                       'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 
                       'Thriller', 'War', 'Western']
        for i, name in enumerate(genre_names):
            if fields[5+i] == '1':
                genres.append(name)
        movie_genres[movie_id] = genres

# Map阶段：输出(类型, (评分,1)) 用于计算平均值
for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) == 4:
        movie_id = fields[1]
        rating = float(fields[2])
        if movie_id in movie_genres:
            for genre in movie_genres[movie_id]:
                print(f"{genre}\t{rating}\t1")
