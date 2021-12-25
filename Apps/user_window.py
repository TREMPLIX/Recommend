import os
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
from services import predict_top10

from app import app

layout = html.Div([

    dcc.Location(id='url-input'),
    html.Div(id='top10'),
    html.Div(id='top_10_movie'),
    html.Button('Получить топ 10 рекомендаций', id='get_top_10', n_clicks=0),
    html.Button('Обновить все фильмы', id='update_scores_table', n_clicks=0),

])


@app.callback(
    Output('top10', 'children'),
    Output('top_10_movie', 'children'),
    Input('get_top_10', 'n_clicks'),
    Input('url-input', 'pathname'))
def get_top_10_movies(n_clicks, pathname):
    user_id = int(pathname.split('/')[-1])
    movies_list = predict_top10.run(user_id)
    df = pd.DataFrame(movies_list, columns=['Название фильма'])
    dt.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns]
    )

    return 'Топ 10 Фильмов для пользователя {}'.format(user_id), df.to_dict('records')
