import pickle
from component.db.sqlite import Sqlite
from model.recsys import RecSys 


def run():
    s = Sqlite('data/db/movie_data.db')
    data_table = s.get_full_data()
    movies = s.get_movie_names()
    rc = RecSys(movies)
    rc.fit(data_table)
    
    with open("data/model/model.pkl", "wb") as f:
        pickle.dump(rc, f)
    print('train is finished')