from dash import html
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP, 'http://127.0.0.1:8050/assets/font.css'],
                suppress_callback_exceptions=True,
                update_title=None,
                title='Bio Right Information',
                use_pages=True)

app._favicon = 'favicon.ico'

server = app.server

app.layout = html.Div([
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
