"""
    The following code is under CC-BY-NC-SA 4.0 license (more in root/LICENSE.txt)
            Free to use and redistribute for any non-commercial purpose
"""

from utils.page_template import portfolio_wrapper
from dash import html
import dash

dash.register_page(__name__, path='/', title='Bio Right Information')

layout = portfolio_wrapper(
    html.Div([
        html.Div([
            html.H1("Biomedical IT",
                    style={'font-weight':'bold',
                           'font-size':'59px',
                           'padding-bottom':'20px',
                           'font-family':'ultraboldFont'}),
            html.H1("Right BIO Intelligence",
                    style={'font-weight': 'normal',
                           'font-size':'24px',
                           'padding-bottom':'20px',
                           'font-family': 'regularFont'}),
            html.H1("""We offer data analytics, data science, and artificial intelligence solutions to examine, organize, find trends, analyze, make predictions, and interpret biomedical data.""",
                    style={'font-weight': 'lighter',
                           'font-size':'24px',
                           'padding-bottom':'20px'}),
            html.H1(
                """We offer end-to-end data integrative science analysis service consisting of solving a data-driven problem and placing them into a context of current scientific knowledge.""",
                style={'font-weight': 'lighter',
                       'font-size': '24px'})
        ],
        style={
            'padding-left':'100px',
            'padding-top':'100px',
            'width':'750px'
        }),
        html.Img(src='assets/DNA.png')
    ],
    style={'display': 'grid',
           'grid-template-columns': '750px 20px auto',
           'grid-auto-flow': 'row'})
)
