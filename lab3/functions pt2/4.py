def average_imdb_score(movies):
    if not movies:
        return 0 

    total_score = sum(movie.get('imdb_rating', 0) for movie in movies)
    average = total_score / len(movies)
    return average

def input_movie_data():
    movies = []
    while True:
        title = input()
        if title.lower() == 'exit':
            break

        imdb_rating = float(input())

        movie = {title,  imdb_rating}
        movies.append(movie)

    return movies

movies_list = input_movie_data()

average_score = average_imdb_score(movies_list)
print(f"Average IMDB score of movies: {average_score:.2f}")