import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
from services import train
from app import app

layout = html.Div([
    html.H1('Admin_window'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'Logs - {}'.format(i[:-4]), 'value': i} for i in os.listdir('data/logs/')
            
        ]
    ),
    html.Div(id='admin_window-display-value'),

    html.Button('Train model', id='train_mdl', n_clicks = 0),
    html.Div(id='admin_window-hitrate')
    
])

@app.callback(
    Output('admin_window-display-value', 'children'),
    Input('admin_window-dropdown', 'value'))

def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('admin_window-hitrate', 'children'),
    Input('train_mdl', 'n_clicks')
)
def update_output(n_clicks):
    k, hr = train.run()
    return 'hit_rate@{} = {}'.format(k, hr)