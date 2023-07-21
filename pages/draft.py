from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
import json

# from utils.pages.genomic_analysis.utils import *
# from utils.pages.genomic_analysis.callbacks import *
from utils.page_template import portfolio_wrapper, TOTAL_WIDTH

def user_message_generator(message,first_node,second_node):
    return \
    html.Div([
        html.Div(message,
                 style={'background-color': 'rgba(111,111,111,0.1)',
                        'padding': '10px', 'border-radius': '15px', "border-bottom-right-radius": "0px"}),
        html.P([
            html.Span('Correlation of',
                      style={'font-weight': '400', 'font-size': '10px', 'color': 'rgba(33,37,41,0.5)'}),
            html.Span(first_node,
                      style={'font-weight': '700', 'font-size': '10px', 'color': 'rgba(33,37,41,0.5)',
                             'padding-left': '4px'}),
            html.Span(' and ',
                      style={'font-weight': '400', 'font-size': '10px', 'color': 'rgba(33,37,41,0.5)',
                             'padding-left': '4px'}),
            html.Span(second_node,
                      style={'font-weight': '700', 'font-size': '10px', 'color': 'rgba(33,37,41,0.5)',
                             'padding-left': '4px'})
        ],
            style={'align-items': 'right', 'justify-content': 'right', 'display': 'grid',
                   'grid-auto-flow': 'row', 'grid-template-columns': 'auto auto auto auto'}),
    ],
        style={'width': '100%', 'align-items': 'right', 'justify-content': 'right', 'display': 'grid',
               'padding-right': '20px','padding-left':'55px'})

def bot_message_generator(message):
    return \
    html.Div([
        html.Div(
            html.Div(
                html.Img(src='assets/genomic_analysis/chat_bot_logo.png'),
                style={'background-color': 'rgba(227,0,15,0.1)','border-radius': '24px',
                       'height':'48px','width':'48px','display':'grid','align-items':'center',
                       'justify-content':'center'})
        ),
        html.Div(),
        html.Div(message,
                 style={'background-color': 'rgba(227,0,15,0.1)',
                        'padding': '10px', 'border-radius': '15px', "border-top-left-radius": "0px"}),
    ],
        style={'width': '100%', 'align-items': 'right', 'justify-content': 'right', 'display': 'grid',
               'padding-right': '64px', 'grid-auto-flow': 'row',
               'grid-template-columns': '48px 7px auto','padding-bottom':'30px'})

def dialog(json_history):
    messages = {}
    for key in json_history:
        if key.startswith('user'):
            messages[int(key.split('-')[1])] = \
                user_message_generator(*json_history[key])
        elif key.startswith('bot'):
            messages[int(key.split('-')[1])+0.1] = \
                bot_message_generator(json_history[key])
        else:
            raise ValueError('Invalid key in json_history')
    return list(map(lambda kv: kv[1], sorted(messages.items())))


dialog_history = {
    'user-0':['What are the results of the given study?','ccRCC','HOXB7'],
    'bot-0':'The results of the study showed that the expression of NIS and TSHR protein was significantly reduced in the thyroid cancer group compared with the normal group.',
    'user-1':['Tell me more about expression of NIS and TSHR protein','ccRCC','HOXB7'],
    'bot-1':'Western blotting results showed that the expression of NIS and TSHR protein was significantly reduced in the thyroid cancer group compared with the normal group. Immunohistochemistry showed the positive expression of NIS and TSHR in thyroid cancer group. The expression of NIS and TSHR mRNA and protein in thyroid cancer patients was significantly lower than that in normal group detected by RT-PCR and Western blotting.'
}

register_page(__name__, title='Bio Right Information')

layout = \
    portfolio_wrapper(
        html.Div([
            html.Div(),
            html.Div(),
            html.Div([
                html.Div([
                    *dialog(dialog_history)
                ],
                style={"width": "624px",
                       "height": "540px",
                       "overflow-y": "auto",
                       "overflow-x": "hidden"},
                    className='custom-personal-scrollbar',
                id='chat-bot-dialog-box'
                ),
                html.Div([
                        dcc.Input(id='user-query-input-2', value='Ask me a question...', type='text',
                                  style={'border-radius': '15px', 'border': '1px solid rgba(227,0,15,0.1)',
                                         'padding-left':'10px',"box-shadow": "0px 0px 35px -12px rgba(227, 0, 17, 1)",
                                         'height':'40px'}),
                        html.Div(),
                        html.Button(
                            html.Div([
                                html.P("Submit",
                                        style={"color": "white", "font-size": "16px", "font-weight": "400",
                                               'padding-top':'6px','padding-right':'5px'}),
                                html.Img(src='assets/genomic_analysis/submit_arrow.png',
                                         style={'padding-bottom':'7px'}),
                            ],
                                style={'display': 'grid',
                                       'grid-template-columns': 'auto auto',
                                       'grid-auto-flow': 'row',
                                       'align-items': 'center',
                                       'justify-content': 'center'}),
                            id='user-query-button-2', n_clicks=0,
                            style={'height':'40px','background-color':'rgba(227,0,17,1)',
                                   'border-radius': '22px', 'border': '0px'})
                    ],
                        style={'display': 'grid',
                               'grid-template-columns': '426px 20px 122px',
                               'grid-auto-flow': 'row',
                               "padding-left": "10px",
                               "padding-top": "10px",
                               }
                    )
            ])
        ],
        style={'display': 'grid',
               'grid-template-columns': f'624px auto 624px',
               'grid-auto-flow': 'row'}
        )
    )


v = \
    html.Div([
        html.Div([
            html.Div(style={
                            "background-color": "#9e9e9e",
                            "border-radius": "20px",
                            "padding-left": "10px",
                            "margin-right": "10px",
                            "padding-top": "10px",
                            "color": "white",
                            "margin-left": "0"
                            },
                     id='user-query-output'
                     ),
            html.Div(),
            html.Div([
                html.Div(style={"padding-left": "20px",
                                "padding-top": "20px",
                                "padding-right": "20px",
                                "padding-bottom": "20px",
                                "width": "80%",
                                "background-color": "#9e9e9e",
                                "border-radius": "20px",
                                "color": "white",
                                "height":"375px",
                                "margin-right": "0"
                                },
                         id='chat-bot-output')
            ],
                style={"display": "flex",
                       "justify-content": "flex-end"})
        ],
            id='dialog-box-history',
            style={"padding-left": "25px",
                   "padding-top": "25px",
                   "padding-right": "25px",
                   "padding-bottom": "25px",
                   "width": "600px",
                   "height": "470px",
                   "display": "grid",
                   'grid-template-rows': '50px 20px 300px'
                   }
        ),
        html.Div([
            html.Div([
                dcc.Input(id='user-query-input', value='Ask me a question...', type='text'),
                html.Div(),
                html.Button('Submit', id='user-query-button', n_clicks=0)
            ],
                style={'display': 'grid',
                       'grid-template-columns': '450px 20px 100px',
                       'grid-auto-flow': 'row',
                       "padding-left": "25px",
                       "padding-top": "20px",
                       }
            )
        ],
            style={"display": "flex",
                   "align-items": "flex-end"}
        )
    ],
        style={"width": "624px",
               "height": "540px",
               "background-color": "#cbcbcb",
               "border-radius": "25px"},
        id='chat-bot-dialog-box')