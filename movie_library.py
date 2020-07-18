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

    def add_to_library(self, type):
        self.type = type
        if self.type == "Film":
            self._library.append(Film("Shrek", "2000", "Comedy", 20))
        elif self.type == "Series":
            self._library.append(Series(title="Friends", year="1990", gendre="Comedy", number_of_vues=900, episode_number=20, season_number=1))
    
    def show_content(self):
        print(self._library)


library = Library()
library.add_to_library("Film")
library.add_to_library("Series")
library.show_content()

