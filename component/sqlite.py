from component.core.sqlite_core import SqliteCore

class Sqlite(SqliteCore):
    
    def __init__(self, database):
        
        super().__init__(database)
        
        
        
    def get_users_data(self, user_id):
        
        query = 'SELECT userId, movieId, rating FROM ratings WHERE userId = {}'.format(user_id)
        return self.get_data(query)
    
    
    
    def get_full_data(self):
        
        query = 'SELECT * FROM ratings'
        return self.get_data(query)
        
    
    
    def get_movie_names(self):
        
        query = 'SELECT * FROM movies'
        return self.get_data(query)
    
    
    
    def get_movies_id(self):
		
        query = 'SELECT movieId FROM movies'
        return self.get_data(query)