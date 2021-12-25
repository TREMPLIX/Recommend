import warnings

warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import pickle
from component.db.sqlite import Sqlite
from component.logs.logs import logging


def create_table():
    lg = logging()
    s = Sqlite('data/db/movie_data.db')
    temp_df = s.get_movie_names()
    temp_df['userId'] = [new_user_id for i in range(temp_df.shape[0])]
    temp_df['rating'] = [-1 for i in range(temp_df.shape[0])]

    return temp_df


def insert_table(temp_df):
    lg = logging()
    new_user_id = s.get_new_user_id()
    insert_df = temp_df[['userId', 'movieId', 'rating']][temp_df['rating'] != -1]
    insert_list = insert_df.values.tolist()

    for i in insert_list:
        s.insert_ratings(i[0], i[1], i[2])

    lg.read_logs('Сделали туту {}'.format(new_user_id))
