import unittest

import os
import sys

sys.path.append('{}/../'.format(os.path.dirname(__file__)))

from model.recsys import RecSys
from component.sqlite import Sqlite


class RecSysTest(unittest.TestCase):

    def test_movies_dict_type(self):
        s = Sqlite('../data/db/movie_data.db')
        data_table = s.get_full_data()
        movies = s.get_movie_names()
        rc = RecSys(movies)
        rc.fit(data_table)

        self.assertTrue(isinstance(rc.movies_dict, dict))

    def test_movies_dict_type(self):
        s = Sqlite('../data/db/movie_data.db')
        data_table = s.get_full_data()
        movies = s.get_movie_names()
        rc = RecSys(movies)
        rc.fit(data_table)

        self.assertTrue(isinstance(rc.users_dict, dict))

    def test_scores_table_type(self):
        s = Sqlite('../data/db/movie_data.db')
        data_table = s.get_full_data()
        movies = s.get_movie_names()
        rc = RecSys(movies)
        rc.fit(data_table)

        self.assertTrue(isinstance(rc.scores_table, dict))


if __name__ == '__main__':
    unittest.main()
