import pickle
import pandas as pd
from component.db.sqlite import Sqlite
from component.logs.logs import logging


def run():
    lg = logging()
    s = Sqlite('data/db/movie_data.db')
    lg.read_logs('Запустили сервис по получению всех пользовательских id')
    return s.get_user_ids()