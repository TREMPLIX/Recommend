import os
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State
from services import add_new_user

df = add_new_user.create_table()

from app import app

layout = html.Div([
    dcc.Location(id='url-input_nuw'),
    dcc.Location(id='url-output_nuw'),

    dt.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),

    html.H5('ФИО'),
    dcc.Textarea(
        id='fio_area_nuw'
    ),
    html.H5('Login'),
    dcc.Textarea(
        id='login_area_nuw'
    ),
    html.H5('Password'),
    dcc.Textarea(
        id='password_area_nuw'
    ),

    html.Button('Сохранить', id='save_nuw', n_clicks=0),

])


@app.callback(
    Output('url-output_nuw', 'pathname'),
    Output('save_nuw', 'n_clicks'),
    Input('url-input_nuw', 'pathname'),
    Input('save_nuw', 'n_clicks'),
    Input('table', 'children'),
    State('fio_area_nuw', 'value'),
    State('login_area_nuw', 'value'),
    State('password_area_nuw', 'value')
)
def create_new_user(pathname, n_clicks, fio_value, login_value, pass_value):
    if n_clicks > 0:
        return '/apps/start_window', 0
