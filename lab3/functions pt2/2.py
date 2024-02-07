def filter_highly_rated_movies(movies):
    return [movie for movie in movies if movie.get('imdb_rating', 0) > 5.5]

def input_movie_data():
    movies = []
    while True:
        title = input("'exit' to stop): ")
        if title.lower() == 'exit':
            break

        imdb_rating = float(input("Enter the IMDB rating: "))

        movie = {'title': title, 'imdb_rating': imdb_rating}
        movies.append(movie)

    return movies

movies_list = input_movie_data()

highly_rated_movies = filter_highly_rated_movies(movies_list)

highly_rated_movies = filter_highly_rated_movies(movies_list)
print("Highly rated movies:", highly_rated_movies)