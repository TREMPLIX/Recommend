import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pickle
from component.db.sqlite import Sqlite
from component.logs_comp import logging


def run():
    lg = logging()
    s = Sqlite('data/db/movie_data.db')
    new_user_id = s.get_new_user_id()

    temp_df = s.get_movie_names()
    temp_df['userId'] = [new_user_id for i in range(temp_df.shape[0])]
    temp_df['rating'] = [-1 for i in range(temp_df.shape[0])]

    # Хорошо было бы получить данные с веб-морды или гуи(вжух)

    temp_df['rating'][temp_df['movieId'] == 12] = 5
    temp_df['rating'][temp_df['movieId'] == 20] = 4
    temp_df['rating'][temp_df['movieId'] == 137] = 3

    insert_df = temp_df[['userId', 'movieId', 'rating']][temp_df['rating'] != -1]
    insert_list = insert_df.values.tolist()

    for i in insert_list:
        s.insert_ratings(i[0], i[1], i[2])

    lg.read_logs('Создали пользователя {}'.format(new_user_id))