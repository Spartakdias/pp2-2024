def is_highly_rated(film_title, imdb_rating):
    return imdb_rating > 5.5

film_title = input()
imdb_rating = float(input())

result = is_highly_rated(film_title, imdb_rating)
print(result)