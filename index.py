import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from Apps import admin_window, start_window, user_window, new_user_window, app2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):

    if '/'.join(pathname.split('/')[:-1]) == '/apps/admin_window':
        return admin_window.layout
    elif '/'.join(pathname.split('/')[:-1]) == '/apps/user_window':
        return user_window.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/start_window':
        return start_window.layout
    elif pathname == '/apps/new_user_window':
        return new_user_window.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=False)