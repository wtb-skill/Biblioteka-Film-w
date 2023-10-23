from random import choice, randint
from typing import List


class Movie:
    def __init__(self, title: str, release_date: str, genre: str, nr_of_plays: int):
        """
        Initialize a Movie object.

        :param title: The title of the movie.
        :param release_date: The release date of the movie.
        :param genre: The genre of the movie.
        :param nr_of_plays: The number of times the movie has been played.
        """
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.nr_of_plays = nr_of_plays

    def __str__(self) -> str:
        """Return a formatted string representation of the movie."""
        return f'{self.title} ({self.release_date})'

    def play(self):
        """Simulate playing the movie and increase the play count."""
        self.nr_of_plays += 1


class TvSeries(Movie):
    def __init__(self, episode_nr: int, season_nr: int, *args, **kwargs):
        """
        Initialize a TV series object.

        :param episode_nr: The episode number.
        :param season_nr: The season number.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.episode_nr = episode_nr
        self.season_nr = season_nr

    def __str__(self) -> str:
        """Return a formatted string representation of the tv series."""
        if int(self.episode_nr) < 10:
            self.episode_nr = '0' + str(self.episode_nr)
        if int(self.season_nr) < 10:
            self.season_nr = '0' + str(self.season_nr)
        return f'{self.title} S{self.season_nr}E{self.episode_nr}'


class FakeDatabase:
    def __init__(self):
        """Initialize a FakeDatabase with pre-defined movie and TV series titles, release dates, and genres."""
        self.movie_titles: List[str] = [
            'The Shawshank Redemption',
            'The Godfather',
            'The Dark Knight',
            'Pulp Fiction',
            'Schindler\'s List',
            'Fight Club',
            'Forrest Gump',
            'The Matrix',
            'Goodfellas',
            'Inception',
            'The Silence of the Lambs',
            'Gladiator',
            'The Lord of the Rings: The Fellowship of the Ring',
            'The Lord of the Rings: The Two Towers',
            'The Lord of the Rings: The Return of the King',
            'The Avengers',
            'The Lion King',
            'Titanic',
            'Jurassic Park',
            'Star Wars: Episode IV - A New Hope',
            'Star Wars: Episode V - The Empire Strikes Back',
            'Star Wars: Episode VI - Return of the Jedi',
            'The Terminator',
            'Terminator 2: Judgment Day',
            'The Green Mile',
            'The Shawshank Redemption',
            'The Godfather',
            'The Dark Knight',
            'Pulp Fiction',
            'Schindler\'s List',
            'Fight Club',
            'Forrest Gump',
            'The Matrix',
            'Goodfellas',
            'Inception',
            'The Silence of the Lambs',
            'Gladiator',
            'The Lord of the Rings: The Fellowship of the Ring',
            'The Lord of the Rings: The Two Towers',
            'The Lord of the Rings: The Return of the King',
            'The Avengers',
            'The Lion King',
            'Titanic',
            'Jurassic Park',
            'Star Wars: Episode IV - A New Hope',
            'Star Wars: Episode V - The Empire Strikes Back',
            'Star Wars: Episode VI - Return of the Jedi',
            'The Terminator',
            'Terminator 2: Judgment Day',
            'The Green Mile'
        ]
        self.tv_series_titles: List[str] = [
            'Breaking Bad',
            'Game of Thrones',
            'Stranger Things',
            'The Crown',
            'The Mandalorian',
            'The Witcher',
            'Friends',
            'The Office',
            'The Big Bang Theory',
            'Sherlock',
            'Westworld',
            'Mindhunter',
            'Narcos',
            'Black Mirror',
            'The Walking Dead',
            'The Simpsons',
            'Lost',
            'The X-Files',
            'The Twilight Zone',
            'Mr. Robot',
            'The Handmaid\'s Tale',
            'Peaky Blinders',
            'Vikings',
            'The Sopranos',
            'Breaking Bad',
            'Game of Thrones',
            'Stranger Things',
            'The Crown',
            'The Mandalorian',
            'The Witcher',
            'Friends',
            'The Office',
            'The Big Bang Theory',
            'Sherlock',
            'Westworld',
            'Mindhunter',
            'Narcos',
            'Black Mirror',
            'The Walking Dead',
            'The Simpsons',
            'Lost',
            'The X-Files',
            'The Twilight Zone',
            'Mr. Robot',
            'The Handmaid\'s Tale',
            'Peaky Blinders',
            'Vikings',
            'The Sopranos'
        ]
        self.release_dates: List[str] = [str(year) for year in range(1950, 2024)]
        self.genres: List[str] = [
            'Fantasy',
            'Superhero',
            'Comedy',
            'Drama',
            'Action',
            'Adventure',
            'Science Fiction',
            'Horror',
            'Thriller',
            'Animation',
            'Mystery',
            'Romance',
            'Crime',
            'Family',
            'Documentary',
            'War',
            'Musical',
            'Western',
            'Historical',
            'Biography'
        ]

    def create_movie(self) -> tuple:
        """
        Create a random movie with title, release date, genre, and set initial play count to 1.

        :return: A tuple containing title, release date, genre, and initial play count.
        """
        random_title = choice(self.movie_titles)
        random_release_date = choice(self.release_dates)
        random_genre = choice(self.genres)
        nr_of_plays = 1
        return random_title, random_release_date, random_genre, nr_of_plays

    def create_series(self) -> tuple:
        """
        Create a random TV series with title, release date, genre, season number, episode number
        and set initial play count to 1.

        :return: A tuple containing title, release date, genre, season number and episode number.
        """
        random_title = choice(self.tv_series_titles)
        random_release_date = choice(self.release_dates)
        random_genre = choice(self.genres)
        season_nr = randint(1, 10)
        episode_nr = randint(10, 20)
        return random_title, random_release_date, random_genre, season_nr, episode_nr





