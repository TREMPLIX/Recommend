import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from services import get_user_ids

from app import app

layout = html.Div([
    dcc.Location(id='url-input_new'),
    dcc.Location(id='url-output_new'),
    html.H5('ФИО'),
    dcc.Textarea(id='fio_area_new'),
    html.H5('Login'),
    dcc.Textarea(id='login_area_new'),
    html.H5('Password'),
    dcc.Textarea(id='password_area_new'),
    html.Button('Сохранить', id='save_new', n_clicks=0),

])


@app.callback(
    Output('url-output_new', 'pathname'),
    Input('url-input_new', 'pathname'),
    Input('save_new', 'n_clicks'),
    State('fio_area_new', 'value'),
    State('login_area_new', 'value'),
    State('password_area_new', 'value')
)
def create_new_user(pathname, n_clicks, fio_value, login_value, pass_value):
    print(fio_value)
    return '/apps/new_user_window'
