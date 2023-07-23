"""
    The following code is under CC-BY-NC-SA 4.0 license (more in root/LICENSE.txt)
            Free to use and redistribute for any non-commercial purpose
"""

from dash import html
import dash
import dash_bootstrap_components as dbc

PORT = 5000
ADDRESS = '127.0.0.1'

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP], # f'http://{ADDRESS}:{PORT}/assets/font.css'
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
    app.run(
        port=PORT,
        host=ADDRESS,
        debug=True
    )