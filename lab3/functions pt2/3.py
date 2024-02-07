def filter_movies_by_category(movies, category):
    return [movie for movie in movies if movie.get('category') == category]

def input_movie_data():
    movies = []
    while True:
        title = input()
        if title.lower() == 'exit':
            break

        category = input()

        movie = {'title': title, 'category': category}
        movies.append(movie)

    return movies

movies_list = input_movie_data()

category_to_filter = input()

filtered_movies = filter_movies_by_category(movies_list, category_to_filter)
print(f"Movies in the category '{category_to_filter}':", filtered_movies)

category_to_filter = 'Action'
filtered_movies = filter_movies_by_category(movies_list, category_to_filter)
print(f"Movies in the category '{category_to_filter}':", filtered_movies)
