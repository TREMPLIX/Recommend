from component.db.core.sqlite_core import SqliteCore
import time

class Sqlite(SqliteCore):

    def __init__(self, database):
        super().__init__(database)

    def get_users_data(self, user_id):
        query = 'SELECT userId, movieId, rating FROM ratings WHERE userId = {}'.format(user_id)
        self.lg.read_logs('Загрузили данные пользовательских рейтингов фильмов для всех пользователей')
        return self.get_data(query)

    def get_full_data(self):
        query = 'SELECT * FROM ratings'
        self.lg.read_logs('Загрузили данные о фильмах')
        return self.get_data(query)

    def get_movie_names(self):
        query = 'SELECT * FROM movies'
        self.lg.read_logs('Загрузили данные id фильмов')
        return self.get_data(query)

    def get_movies_id(self):
        query = 'SELECT movieId FROM movies'
        return self.get_data(query)

    def get_new_user_id(self):
        query = 'SELECT userId FROM ratings'
        self.lg.read_logs('Получение ID для нового пользователя')
        new_user_id = max(set(self.get_data(query)['userId'].values.tolist())) + 1
        return new_user_id

    def insert_ratings(self, user_id, movie_id, score):
        query = 'INSERT INTO ratings (userId, movieId, rating, timestamp) VALUES ({}, {}, {}, {})'.format(user_id, movie_id, score, time.time())
        self.lg.read_logs('Пользователь {} поставил оценку {} фильму {}'.format(user_id, score, movie_id))
        self.update_table(query)

    def update_ratings(self, user_id, movie_id, score):
        query = 'UPDATE ratings SET rating = {}, timestamp = {} WHERE userId = {} AND movieId = {}'.format(score, time.time(), user_id, movie_id)
        self.lg.read_logs('Пользователь {} обновил оценку {} фильму {}'.format(user_id, score, movie_id))
        self.update_table(query)