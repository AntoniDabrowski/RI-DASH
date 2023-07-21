from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

TOTAL_WIDTH = 1320

def portfolio_wrapper(*BODY):
    return \
        html.Div([
            # Header
            html.Div(
                html.Div([
                    html.Div(
                        html.Img(
                            src='https://rightinformation.com/wp-content/uploads/2021/10/Right-Information-Tabliczka-black.svg'),
                    ),
                    html.Div(),
                    html.Div(
                        dbc.NavItem(
                            dbc.NavLink(
                                html.H1("Company",
                                        style={
                                            'font-size':'16px',
                                            'font-weight':'400'
                                        }),
                                    href="/",
                                    id='company-button-id')),
                        style={'margin': 'auto',
                               'padding-top':'6px',
                               'width':'100%',
                               'height':'100%'}),
                    html.Div(),
                    html.Div(
                        dbc.Nav([
                            dbc.DropdownMenu(
                                caret=False,
                                label=html.H1("Portfolio",
                                              style={'font-size':'16px',
                                                     'color':'black',
                                                     'font-weight':'400'}),
                                menu_variant='dark',
                                children=[
                                    dbc.DropdownMenuItem(
                                        dbc.NavLink(
                                            html.H1("Genomic analysis",
                                                style={'font-size':'16px',
                                                'color':'white',
                                                'font-weight':'400'}),
                                            href="/genomic-analysis")
                                    ),
                                ],
                                nav=True,
                                in_navbar=True,
                                color="rgba(241,241,241,1)"
                            )
                        ]),
                        id='portfolio-button-id',
                        style={'display':'grid',
                               'height':'100%'}),
                    html.Div(),
                    html.Div("Services", id='services-button-id',
                             style={'margin': 'auto',
                                    'padding-top':'6px',
                                    'width':'100%',
                                    'height':'100%'}),
                    html.Div(),
                    html.Div(
                        dbc.NavLink(
                            html.Div('Contact us',
                                     style={'text-align': 'center',
                                            'padding-top':'6px'}),
                            href='https://rightinformation.com/contact-us/'
                        ),
                        id='contact-us-button-id',
                        style={'border': '1px solid red',
                               'width': '195px',
                               'height': '40px',
                               'border-radius': '20px'})
                ],
                    style={'padding-right': '50px',
                           'height': '106px',
                           'padding-top': '10px',
                           'padding-bottom': '10px',
                           'display': 'grid',
                           'grid-template-columns': '195px auto 60px 57px 60px 83px 60px 70px 195px',
                           'grid-auto-flow': 'row'}),
                style={
                    'padding-top': '28px',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'width': f'{TOTAL_WIDTH}px'
                }
            ),
            # Body
            html.Div([
                *BODY
            ],
                id='page-body-id',
                style={
                    'padding-top': '10px',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'width': f'{TOTAL_WIDTH - 30}px'
                }),
        ],
            id='main-page-content',
            style={'backgroundColor': 'rgb(241,241,241)',
                   'min-height': '1200px',
                   'min-width': f'{TOTAL_WIDTH}px',
                   'padding-bottom':'100px'
                   }
        )
