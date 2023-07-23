"""
    The following code is under CC-BY-NC-SA 4.0 license (more in root/LICENSE.txt)
            Free to use and redistribute for any non-commercial purpose
"""

import pickle
import numpy as np
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash
import plotly.graph_objs as go

@dash.callback([Output("progress_bar", "value"), Output("progress_bar", "label")],
               Input('interval-component', 'n_intervals'))
def update_progress_bar(n):
    return n / 2, f'{n * 50 + np.random.randint(0, 50)}' if n >= 15 else ""

@dash.callback(Output("progress_bar_wrapper", "style"),
               Input('interval-component', 'n_intervals'))
def update_progress_bar_style(n):
    if n >= 3:
        return {'padding-left': '25px',
                'display': 'flex',
                'z-index': '5'}
    return {'display': 'none'}

@dash.callback([Output('live-update-graph', 'figure'), Output('relation-map', 'style')],
               Input('interval-component', 'n_intervals'),
               [State('relation-map', 'style'),State('selected-node-I','children'),State('selected-node-II','children')])
def update_graph_live(n, style, selected_node_I, selected_node_II):
    # print(f"ITERATION {n}")
    fig_path = f'data/genomic_analysis/figures/fig_{n}.pickle'
    if n < 1:
        raise PreventUpdate
    elif n == 1:
        figure = pickle.load(open(fig_path, 'rb'))
        style['visibility'] = 'hidden'
    else:
        hover_data_path = f'data/genomic_analysis/hover_data/hover_data_{n}.pickle'
        url_path = f'data/genomic_analysis/urls.pickle'
        hover_path = f'data/genomic_analysis/hovers.pickle'

        figure = pickle.load(open(fig_path, 'rb'))
        hover_data = pickle.load(open(hover_data_path, 'rb'))
        urls = pickle.load(open(url_path, 'rb'))
        hovers = pickle.load(open(hover_path, 'rb'))

        # add scatter
        for x_coordinates, y_coordinates, url, hover in zip(hover_data['x_coordinates'],
                                                            hover_data['y_coordinates'],
                                                            urls, hovers):
            scatter = go.Scatter(
                x=np.linspace(x_coordinates[0], x_coordinates[1], endpoint=False)[1:],
                y=np.linspace(y_coordinates[0], y_coordinates[1], endpoint=False)[1:],
                customdata=[(f"title: {url}", url)] * 49,
                marker=dict(
                    opacity=0,
                    color="rgba(0,0,0,0)"),
                showlegend=False,
                hovertemplate=hover)
            figure.add_trace(scatter)

        style['visibility'] = 'visible'
    figure.update_layout(
        width=624,
        height=624,
        legend=dict(
            orientation="h",
            yanchor="top",
            xanchor="center",
            y=0.0,
            x=0.5),
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=0
        )
    )

    if n>4:
        highlights = pickle.load(open('data/genomic_analysis/highlight.pickle','rb'))
        line_1 = highlights.get((selected_node_I, selected_node_II), None)
        line_2 = highlights.get((selected_node_II, selected_node_I), None)
        line = line_1 if line_1 is not None else line_2
        hover_data_path = f'data/genomic_analysis/hover_data/hover_data_{min(200,n)}.pickle'
        hover_data = pickle.load(open(hover_data_path, 'rb'))
        X = hover_data['x_coordinates'][line]
        Y = hover_data['y_coordinates'][line]
        highlight_fig = go.Scatter(x=X, y=Y, mode='lines', line=dict(color='rgba(35, 177, 40, 0.5)', width=7),showlegend=False)
        figure.data = figure.data[::-1]
        figure.add_trace(highlight_fig)
        figure.data = figure.data[::-1]


    return figure, style

@dash.callback(Output('interval-component', 'n_intervals'),
               Input('reload-button', 'n_clicks'),
               State('interval-component', 'n_intervals'))
def interval_update(n_clicks, current_value):
    if n_clicks > 0:
        return 0
    return current_value
