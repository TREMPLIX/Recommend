import pickle
import pandas as pd
from component.db.sqlite import Sqlite
from component.logs_comp import logging


# from helper import text_processing as tp

def run(user_id):

    lg = logging()
    with open("data/model/model.pkl", 'rb') as f:
        rc = pickle.load(f)
    lg.write_logs('Загрузили модель')
    test_table = pd.DataFrame()

    s = Sqlite('data/db/movie_data.db')
    test_table['movieId'] = s.get_movies_id()

    test_table['userId'] = [user_id for i in range(test_table.shape[0])]
    predict_data = rc.predict(test_table[['userId', 'movieId']], get_name=True)
    predict_data_df = pd.DataFrame(predict_data, columns=['scores', 'movie_name'])
    film_names_top10 = predict_data_df.sort_values(by='scores', ascending=False).head(10)['movie_name'].values.tolist()

    print(film_names_top10)
