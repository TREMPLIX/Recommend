import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pickle
from component.db.sqlite import Sqlite
from component.logs_comp import logging


def run(user_id):
    lg = logging()
    s = Sqlite('data/db/movie_data.db')
    exists_user_df = s.get_users_data(user_id)
    exists_user_df['status'] = [1 for i in range(exists_user_df.shape[0])]
    exists_user_df['updstatus'] = [0 for i in range(exists_user_df.shape[0])]

    all_movie_df = s.get_movie_names()['movieId']

    non_exists_movie_id = list(set(all_movie_df.values.tolist()).difference(set(exists_user_df['movieId'].values.tolist())))

    non_exists_user_df = pd.DataFrame()
    non_exists_user_df['movieId'] = non_exists_movie_id
    non_exists_user_df['rating'] = [-1 for i in range(non_exists_user_df.shape[0])]
    non_exists_user_df['userId'] = [user_id for i in range(non_exists_user_df.shape[0])]
    non_exists_user_df['status'] = [0 for i in range(non_exists_user_df.shape[0])]
    non_exists_user_df['updstatus'] = [0 for i in range(non_exists_user_df.shape[0])]

    full_df = exists_user_df.append(non_exists_user_df[['userId', 'movieId', 'rating', 'status', 'updstatus']])

    # Хорошо было бы получить данные с веб-морды или гуи(вжух)

    full_df['rating'][full_df['movieId'] == 1] = 5
    full_df['updstatus'][full_df['movieId'] == 1] = 1

    full_df['rating'][full_df['movieId'] == 2] = 4
    full_df['updstatus'][full_df['movieId'] == 2] = 1

    full_df['rating'][full_df['movieId'] == 3] = 3
    full_df['updstatus'][full_df['movieId'] == 3] = 1

    upd_df = full_df[full_df['updstatus'] == 1]
    upd_list = upd_df.values.tolist()

    for i in upd_list:
        if i[3] == 1:
            s.update_ratings(i[0], i[1], i[2])
        elif i[3] == 0:
            s.insert_ratings(i[0], i[1], i[2])
        else:
            lg.write_logs('Некорректный формат статуса существования оценки фильма')