from faker import Faker
import random

class Film:
    def __init__(self, title, year, gendre, number_of_vues):
        self.title = title
        self. year = year
        self.gendre = gendre
        self.number_of_vues = number_of_vues

    def play(self):
        self.number_of_vues += 1

    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Film):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    
    def __str__(self):
        return f"{self.title} S{self.episode_number:02d}E{self.season_number:02d}"


class Library:
    def __init__(self):
        self._library = []

    def add_to_library(self, type, *args, **kwargs):
        self.type = type
        if self.type == "Film":
            self._library.append(Film(*args, **kwargs))
        elif self.type == "Series":
            self._library.append(Series(*args, **kwargs))
    
    def show_content(self):
        for item in self._library:
            print(item)
    
    def get_movies(self):
        movies_list = [item for item in self._library if "Film" in str(type(item))]
        return movies_list

    def get_series(self):
        series_list = [item for item in self._library if "Series" in str(type(item))]
        return series_list      

    def search(self, title):
        self.title = title
        found_value = [item for item in self._library if item.title == self.title]
        return found_value

    def multiply_generate_views(func):
        def wrapper(*args, **kwargs):
            for i in range(10):
                func(*args, **kwargs)
        return wrapper

    @multiply_generate_views
    def generate_views(self):
        random_index = random.randrange(len(self._library))
        element = self._library[random_index]
        element.number_of_vues += random.randrange(1,100)
        print(element, element.number_of_vues)

    def top_titles(self, content_type):
        self.content_type = content_type
        library_type = [item for item in self._library if self.content_type in str(type(item))]
        top_titles_list = sorted(self._library, key=lambda object: object.number_of_vues)[0:3]
        return top_titles_list

fake = Faker("fr_FR")

library = Library()
library.add_to_library("Film", title="Shrek", year="2000", gendre="Comedy", number_of_vues=90)
library.add_to_library("Film", title="Harry Potter", year="2010", gendre="Fantasy", number_of_vues=2000)
library.add_to_library("Film", title="Bridget Jones", year="2005", gendre="Comedy", number_of_vues=90)
library.add_to_library("Series", title="Friends", year="1990", gendre="Comedy", number_of_vues=900, episode_number=20, season_number=1)
library.add_to_library("Series", title="House of Cards", year="2013", gendre="Thriller", number_of_vues=900, episode_number=10, season_number=2)
library.add_to_library("Series", title="Game of Thrones", year="2010", gendre="Drama", number_of_vues=100, episode_number=2, season_number=9)
library.add_to_library("Series", title="Californication", year="2007", gendre="Comedy-Drama", number_of_vues=100, episode_number=30, season_number=1)

library.show_content()
library.generate_views()
print("-------------------------")
top_titles = library.top_titles("Series")

for i in top_titles:
    print(i)





