import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from services import get_user_ids

from app import app

layout = html.Div([
    dcc.Location(id='url-input_sw'),
    dcc.Location(id='url-output_sw'),
    html.H5('login'),
    dcc.Textarea(
        id='login_area_sw'
    ),

    html.H5('password'),
    dcc.Textarea(
        id='password_area_sw'
    ),

    html.Button('Register', id='reg_sw', n_clicks=0),
    html.Button('Sign in', id='sign_sw', n_clicks=0),

])


@app.callback(
    Output('url-output_sw', 'pathname'),
    Output('sign_sw', 'n_clicks'),
    Output('reg_sw', 'n_clicks'),
    Input('sign_sw', 'n_clicks'),
    Input('reg_sw', 'n_clicks'),
    State('login_area_sw', 'value'),
    State('password_area_sw', 'value'),

)
def update_output(n_clicks_sign, n_clicks_reg, value_login, value_pass):
    if n_clicks_sign > 0:
        user_ids = get_user_ids.run()
        if value_login == 'admin' and value_pass == 'admin':
            return '/apps/admin_window/{}'.format(value_login), 0, 0
        elif int(value_login) in user_ids and value_pass == '0000':
            return'apps/user_window/{}'.format(value_login), 0, 0
    elif n_clicks_reg > 0:
        return 'apps/new_user_window', 0, 0

