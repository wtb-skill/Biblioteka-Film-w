from model import Movie, TvSeries, FakeDatabase
from random import randint
from datetime import datetime as dt
from typing import List, Optional, Union


class Library:
    def __init__(self):
        """
        Initialize the Library class with an empty collection.
        """
        self.collection = []

    def add_movie(self, title: str, release_date: str, genre: str, nr_of_plays: int):
        """
        Add a movie to the collection.

        :param title: The title of the movie.
        :param release_date: The release date of the movie.
        :param genre: The genre of the movie.
        :param nr_of_plays: The number of times the movie has been played.
        :return: None
        """
        movie = Movie(
            title=title,
            release_date=release_date,
            genre=genre,
            nr_of_plays=nr_of_plays
        )
        self.collection.append(movie)

    def add_series(self, title: str, release_date: str, genre: str, nr_of_plays: int, episode_nr: int, season_nr: int):
        """
        Add a TV series to the collection.

        :param title: The title of the TV series.
        :param release_date: The release date of the TV series.
        :param genre: The genre of the TV series.
        :param nr_of_plays: The number of times the TV series has been played.
        :param episode_nr: The episode number of the TV series.
        :param season_nr: The season number of the TV series.
        :return: None
        """
        series = TvSeries(
            title=title,
            release_date=release_date,
            genre=genre,
            nr_of_plays=nr_of_plays,
            episode_nr=episode_nr,
            season_nr=season_nr
        )
        self.collection.append(series)

    def get_movies(self) -> List[Movie]:
        """
        Get a sorted list of all movies in the collection.

        :return: List of movies
        """
        movies_list = [_entry for _entry in self.collection if isinstance(_entry, Movie)]
        sorted_movies_list = sorted(movies_list, key=lambda _entry: _entry.title)
        return sorted_movies_list

    def get_series(self) -> List[TvSeries]:
        """
        Get a sorted list of all TV series in the collection.

        :return: List of TV series
        """
        series_list = [_entry for _entry in self.collection if isinstance(_entry, TvSeries)]
        sorted_series_list = sorted(series_list, key=lambda _entry: _entry.title)
        return sorted_series_list

    def search(self, title: str) -> List[Union[Movie, TvSeries]]:
        """
        Search the collection for entries with a given title.

        :param title: The title to search for.
        :return: List of entries matching the title.
        """
        result = [_entry for _entry in self.collection if _entry.title == title]
        return result

    def generate_views(self):
        """
        Generate random views for a random entry in the collection.
        """
        max_index = len(self.collection) - 1
        random_entry = self.collection[randint(0, max_index)]
        views_nr = randint(1, 100)
        for _ in range(views_nr):
            random_entry.play()

    def paid_viewer_bots(self):
        """
        Activate generate_views 10 times.
        """
        for _ in range(10):
            self.generate_views()

    def top_titles(self, top: int, content_type: Optional[str] = None) -> List[Union[Movie, TvSeries]]:
        """
        Get the top-rated entries in the collection.

        :param top: The number of top entries to retrieve.
        :param content_type: The content type ('movies', 'series') to filter by.
        :return: List of the top-rated entries.
        """
        if content_type == 'movies':
            sorted_list = sorted(self.get_movies(), key=lambda _entry: _entry.nr_of_plays, reverse=True)
        elif content_type == 'series':
            sorted_list = sorted(self.get_series(), key=lambda _entry: _entry.nr_of_plays, reverse=True)
        else:
            sorted_list = sorted(self.collection, key=lambda _entry: _entry.nr_of_plays, reverse=True)
        return sorted_list[:top]

    def add_full_seasons(self, title: str, release_date: str, genre: str, season_nr: int, episode_nr: int):
        """
        Add a full season of a TV series to the collection.

        :param title: The title of the TV series.
        :param release_date: The release date of the TV series.
        :param genre: The genre of the TV series.
        :param season_nr: The season number.
        :param episode_nr: The number of episodes in the season.
        """
        for episode in range(1, episode_nr + 1):
            series = TvSeries(
                title=title,
                release_date=release_date,
                genre=genre,
                season_nr=season_nr,
                episode_nr=episode,
                nr_of_plays=1
            )
            self.collection.append(series)

    def display_episode_count(self, title: str) -> int:
        """
        Display the number of episodes for a TV series with a given title.

        :param title: The title of the TV series.
        :return: The number of episodes for the TV series.
        """
        count = 0
        for episode in self.get_series():
            if episode.title == title:
                count += 1
        return count

    def initialise_database(self):
        """
        Initialize the library's database with fake movie and series entries.
        """
        fake_database = FakeDatabase()
        for _ in range(50):
            fake_movie = fake_database.create_movie()
            self.add_movie(*fake_movie)
            fake_series = fake_database.create_series()
            self.add_full_seasons(*fake_series)


if __name__ == "__main__":
    print("Biblioteka filmów")
    biblioteka = Library()
    biblioteka.initialise_database()
    biblioteka.paid_viewer_bots()
    today = str(dt.today()).split(" ")[0]
    print(f"Najpopularniejsze filmy i seriale dnia {today}:")
    top_3 = biblioteka.top_titles(3)
    for entry in top_3:
        print(entry)
