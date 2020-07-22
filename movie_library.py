import random
from datetime import date


def multiply_generate_views(func):
    def wrapper(*args, **kwargs):
        for i in range(1000):
            func(*args, **kwargs)
    return wrapper


class Film:
    def __init__(self, title: str, year: str, gendre: str, number_of_vues: int = 0):
        self.title = title
        self. year = year
        self.gendre = gendre
        self.number_of_vues = number_of_vues

    def play(self):
        self.number_of_vues += 1

    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Film):
    def __init__(self, episode_number: int, season_number: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.episode_number:02d}E{self.season_number:02d}"


class Library:
    def __init__(self):
        self._library: list = []

    def add_to_library(self, type: str, *args, **kwargs):
        if type == "Film":
            self._library.append(Film(*args, **kwargs))
        elif type == "Series":
            self._library.append(Series(*args, **kwargs))

    def show_content(self):
        for item in self._library:
            print(item)

    def get_movies(self) -> list:
        movies_list = [item for item in self._library if "Film" in str(type(item))]
        return movies_list

    def get_series(self) -> list:
        series_list = [item for item in self._library if "Series" in str(type(item))]
        return series_list

    def search(self, title: str) -> list:
        found_value = [item for item in self._library if item.title == title]
        return found_value

    @multiply_generate_views
    def generate_views(self):
        random_index = random.randrange(len(self._library))
        element = self._library[random_index]
        element.number_of_vues += random.randrange(1, 100)

    def top_titles_type(self, content_type: dict(type=str, help="Film or Series")) -> list:
        library_type = [item for item in self._library if content_type in str(type(item))]
        top_titles_list = sorted(library_type, key=lambda item: item.number_of_vues)[0:3]
        return top_titles_list

    def top_titles(self) -> list:
        top_titles_list = sorted(
            self._library, key=lambda item: item.number_of_vues)[0:3]
        return top_titles_list

    def show_nr_of_episodes(self, title: str) -> int:
        list_of_episodes = [item for item in self._library if item.title == title]
        number_of_episodes = len(list_of_episodes)
        return number_of_episodes


def add_season(
                s_title: str, s_year: str, s_gendre: str,
                s_season_number: int, number_of_episodes: int) -> list:
    for i in range(1, int(number_of_episodes) + 1):
        library.add_to_library(
                                "Series", title=s_title, year=s_year, gendre=s_gendre,
                                episode_number=i, season_number=s_season_number)




if __name__ == "__main__":

    print("Biblioteka fimów")

    library = Library()
    library.add_to_library(
                            "Film", title="Shrek", year="2000",
                            gendre="Comedy", number_of_vues=9651610)
    library.add_to_library(
                            "Film", title="Harry Potter",
                            year="2010", gendre="Fantasy",
                            number_of_vues=20000)
    library.add_to_library(
                            "Film", title="Bridget Jones",
                            year="2005", gendre="Comedy",
                            number_of_vues=179516510)
    library.add_to_library(
                            "Film", title="Iron Man",
                            year="2005", gendre="SuperHero",
                            number_of_vues=11115600)
    library.add_to_library(
                            "Film", title="Star Wars",
                            year="1999", gendre="Science-fiction",
                            number_of_vues=90165354)

    add_season(
                s_title="Friends", s_year="1990",
                s_gendre="Comedy", s_season_number=1,
                number_of_episodes=12)
    add_season(
                s_title="House of Cards", s_year="2013",
                s_gendre="Thriller", s_season_number=2,
                number_of_episodes=13)
    add_season(
                s_title="Game of Thrones", s_year="2010",
                s_gendre="Drama", s_season_number=1,
                number_of_episodes=6)
    add_season(
                s_title="Young Sheldon", s_year="2018",
                s_gendre="Comedy", s_season_number=1,
                number_of_episodes=15)
    add_season(
                s_title="Desperate Housewifes", s_year="2010",
                s_gendre="Comedy", s_season_number=8,
                number_of_episodes=10)
    add_season(
                s_title="Gladiator", s_year="2008", s_gendre="Drama",
                s_season_number=3, number_of_episodes=9)


    library.generate_views()

    top_3_series = library.top_titles_type("Series")
    top_3_movies = library.top_titles_type("Film")

    today = date.today().strftime("%d.%m.%Y")
    top_3 = library.top_titles()
    print(f"Najpopularniejsze filmy i seriale dnia {today}")
    for i in top_3:
        print(i)
    print("---------Top 3 filmy:")
    for i in top_3_movies:
        print(i)
    print("---------Top 3 seriale:")
    for i in top_3_series:
        print(i)
