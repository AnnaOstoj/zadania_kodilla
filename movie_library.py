class Film:
    def __init__(self, title, year, gendre, number_of_vues):
        self.title = title
        self. year = year
        self.gendre = gendre
        self.number_of_vues = number_of_vues

    def play(self):
        self.number_of_vues += 1
        return number_of_vues

    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Film):
    def __init__(self, episode_number, season_number, *args, **kwargs)
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    
    def __str__(self):
        return f"{self.title} S{self.episode_number}E{self.season_number}"

