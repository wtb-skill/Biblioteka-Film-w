class Movie:
    def __init__(self, title, release_date, genre, nr_of_plays):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.nr_of_plays = nr_of_plays

    def __str__(self) -> str:
        """Return a formatted string representation of the movie."""
        return f'{self.title} ({self.release_date})'

    def play(self):
        self.nr_of_plays += 1


class TvSeries(Movie):
    def __init__(self, episode_nr, season_nr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_nr = episode_nr
        self.season_nr = season_nr

    def __str__(self) -> str:
        """Return a formatted string representation of the tv series."""
        return f'{self.title} S{self.season_nr}E{self.episode_nr}'


library = [
    Movie(title='Lord of The Rings', release_date='2002', genre='fantasy', nr_of_plays=20),
    Movie(title='Avengers', release_date='2006', genre='super-hero', nr_of_plays=33),
    TvSeries(title='The Simpsons', release_date='1995', genre='cartoon', nr_of_plays=20,
             episode_nr=28, season_nr='02'),
    TvSeries(title='Game of Thrones', release_date='2016', genre='fantasy', nr_of_plays=33,
             episode_nr=11, season_nr='05')
]

for entry in library:
    print(entry)

