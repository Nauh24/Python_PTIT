class MovieCategory:
    def __init__(self, category_id, name):
        self.id = category_id
        self.name = name

class Movie:
    def __init__(self, movie_id, category, date, name, count):
        self.id = movie_id
        self.category = category
        self.date = date
        self.day = int(date[0:2])
        self.month = int(date[3:5])
        self.year = int(date[6:])
        self.name = name
        self.count = count

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.category.name, self.date, self.name, self.count)


num_categories, num_movies = [int(i) for i in input().split()]
movie_categories = []
movies = []

for i in range(num_categories):
    movie_categories.append(MovieCategory('TL{:03}'.format(i + 1), input()))

for i in range(num_movies):
    category_id = input()
    for category in movie_categories:
        if category_id == category.id:
            movies.append(Movie('P{:03}'.format(i + 1),
                                category, input(), input(), int(input())))

movies.sort(key=lambda e: (e.year, e.month, e.day, e.name, -e.count))
for movie in movies:
    print(movie)
