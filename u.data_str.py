with open('u.item', encoding='latin-1') as f_in:
    with open('u.item.genres', 'w', encoding='utf-8') as f_out:
        for line in f_in:
            fields = line.strip().split('|')
            movie_id = fields[0]
            title = fields[1]
            imdb_url = fields[4]  # IMDb URL，第5列
            
            genre_names = ['unknown', 'Action', 'Adventure', 'Animation', "Children's", 
                           'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 
                           'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 
                           'Sci-Fi', 'Thriller', 'War', 'Western']
            
            genres_list = []
            for i, name in enumerate(genre_names):
                if fields[5+i] == '1':
                    genres_list.append(name)
            
            genres_str = ','.join(genres_list)
            # 新格式：movie_id|title|imdb_url|genres
            f_out.write(f"{movie_id}|{title}|{imdb_url}|{genres_str}\n")
