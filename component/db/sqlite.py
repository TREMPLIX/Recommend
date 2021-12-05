from component.db.core.sqlite_core import SqliteCore


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
