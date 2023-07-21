from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import os
import inspect
import dash
from utils.page_template import portfolio_wrapper, TOTAL_WIDTH
from utils.pages.publication_summarization.utils import *
from utils.pages.publication_summarization.callbacks import *

dash.register_page(__name__, title='Bio Right Information')

layout = portfolio_wrapper(
    html.Br(),
    html.Div(table_description,
             style={'width':f'{TOTAL_WIDTH-200}px',
                    'margin':'auto'}),
    html.Div([
        dash_table.DataTable(data=table_data,
                             columns=table_columns,
                             id='table',
                             style_cell={'textAlign': 'left'},
                             style_data={
                                 'height': 'auto',
                                 'whiteSpace': 'pre-line'
                             },
                             css=[{
                                 'selector': '.dash-spreadsheet td div',
                                 'rule': '''width: 1000px'''
                             }],
                             ),
    ],
        style={'width': '850px',
               'padding-top': '50px',
               'margin':'auto'},
        id='specification-table'),
    dbc.Popover(
        [
            dbc.PopoverHeader("Knowledge base analysis"),
            dbc.PopoverBody
            ("The table shows the key insights taken from over 1000 publications discussing the relation between given cancer type and highlighted elements. Answers were made by our specialized information retrieval system")
        ],
        id="specification-table-popover",
        is_open=False,
        trigger="hover",
        target="specification-table",
    )
)
