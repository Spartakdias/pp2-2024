def filter_highly_rated_movies(movies):
    return [movie for movie in movies if movie.get('imdb_rating', 0) > 5.5]

def input_movie_data():
    movies = []
    while True:
        title = input()
        if title.lower() == 'exit':
            break

        imdb_rating = float(input())

        movie = {'title': title, 'imdb_rating': imdb_rating}
        movies.append(movie)

    return movies

movies_list = input_movie_data()

highly_rated_movies = filter_highly_rated_movies(movies_list)
print( highly_rated_movies)