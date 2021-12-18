import pickle
from component.db.sqlite import Sqlite
from model.recsys import RecSys
from model.metrics import evaluate
from component.logs_comp import logging


def run():

    lg = logging()
    s = Sqlite('data/db/movie_data.db')
    data_table = s.get_full_data()
    movies = s.get_movie_names()
    rc = RecSys(movies)
    rc.fit(data_table)

    pred_data = rc.predict(data_table[['userId', 'movieId']])
    data_table_pred = data_table.copy()
    data_table_pred['rating'] = pred_data

    k = 10
    hr = evaluate(data_table_pred, data_table, k)
    lg.write_logs('hit_rate@{} = {}'.format(k, hr))

    with open("data/model/model.pkl", "wb") as f:
        pickle.dump(rc, f)
    print('train is finished')
    return k, hr