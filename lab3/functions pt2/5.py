def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie.get('category') == category]
    
    if not category_movies:
        return 0 

    total_score = sum(movie.get('imdb_rating', 0) for movie in category_movies)
    average = total_score / len(category_movies)
    return average

def input_movie_data():
    movies = []
    while True:
        title = input()
        if title.lower() == 'exit':
            break

        category = input()
        imdb_rating = float(input())

        movie = {'title': title, 'category': category, 'imdb_rating': imdb_rating}
        movies.append(movie)

    return movies