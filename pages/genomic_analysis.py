"""
    The following code is under CC-BY-NC-SA 4.0 license (more in root/LICENSE.txt)
            Free to use and redistribute for any non-commercial purpose
"""

from dash import dcc, register_page, dash_table
import dash_bootstrap_components as dbc
import visdcc

from utils.pages.genomic_analysis.utils import *
from utils.pages.genomic_analysis.callbacks import *
from utils.page_template import portfolio_wrapper

register_page(__name__, title='Bio Right Information')

chapter_headline = \
    html.Div([
        html.Div([
            html.Div(style={'height':'100px'}),
            html.Span('AI-based gene expression profiling',
                    style={
                        'width':'500px',
                        'font-size':'40px',
                        'font-weight':'600',
                        'height':'auto',
                        'font-family': 'ultraboldFont'
                    }),
            html.P('Gene expression profiling has been successfully used to classify different types of tumours such as breast, melanoma, lung and other. However, it is difficult to combine the insights for these studies into a more coherent and meaningful analysis that guide the next research step and could result in a quicker diagnosis, development of novel drugs or personalized therapies.',
                style = {
                    'text-align': 'justify',
                    'text-justify': 'inter-word',
                    'font-family': 'roboto-light',
                }
            ),
            html.Div(style={'height':'100px'}),
            html.Div(
                html.H1("Case study results:",
                        style={
                            'font-family': 'regularFont',
                            'font-size':'40px'}),
                    style={
                        'height':'100px',
                        'display': 'flex',
                        'align-items': 'flex-end'}
            )
        ],
            style={'display':'grid','padding-left':'50px'}),
        html.Img(src='assets/genomic_analysis/stock-3.png',
                 # make it in the middle
                 style={'display': 'grid',
                        'margin-left': 'auto',
                        'margin-right': 'auto',
                        'padding-top': '100px',
                        'padding-bottom': '20px'}
                 )
        ],
        style={'border-bottom':'solid black 1px','display':'grid','grid-template-columns':'600px auto','height':'580px',
               'grid-auto-flow':'row'}
    )


chapter_models = \
    html.Div([
        html.Div([
            html.H1("Creating state-of-the-art models",
                    style={
                        'font-family': 'regularFont',
                        'font-size':'40px',
                    }),
            html.Div([
                html.Img(src='assets/arrow.jpg'),
                html.P([
                    html.Span("This research aims to identify the most relevant genes for cancer prediction. We used a dataset from the recount2 project, which combines records of many separate clinical trials. In order to check data usefulness, we had to assess if there is a possibility of distinguishing between healthy and sick people based on the information hidden within gene expression records. To do that we replicated methodology from the relevant publication."),
                    html.Br(),
                    html.Br(),
                    html.Span("The graph below displays the accuracy that our models achieved in different cancer type groups (COAD_stage, KIRC_stage, LIHC_stage, etc.). Each group shows the cloud of dots, that represent the measured accuracy of each tested model or hyperparameter setting. The highlighted points are results from the referenced study and our best result (average from cross-validation trial).")
                ],
                    style = {
                        'text-align': 'justify',
                        'text-justify': 'inter-word',
                        'padding-top':'20px',
                        'font-family': 'roboto-light',
                    })
            ],
            style={
                'display':'grid',
                'grid-template-columns':'130px auto',
                'grid-auto-flow':'row',
                'padding-bottom':'30px'}),
            html.Img(src='assets/genomic_analysis/model_comparison.png'),
        ],
            style={'padding-top':'35px','padding-bottom':'50px'}
        ),
        html.Div([
                html.Div(style={'background-color':'black','height':'1px'}),
                html.Div()
        ],
            style={'display':'grid','grid-template-columns':'720px auto','grid-auto-flow':'row','height':'1px'})
    ])


chapter_genes = \
    html.Div([
        html.Div([
            html.Img(src='assets/genomic_analysis/most_discriminating_genes.png',
                     style={'display': 'block','margin-left':'-90px'}),
            html.Div([
                html.H1("Top discriminating genes",
                        style={
                            'font-family': 'regularFont',
                            'font-size':'40px'}),
                html.Div([
                    html.Img(src='assets/arrow.jpg'),
                    html.P("Once we found the right way of classifying patients into different cancer groups, we tested the model in order to assess on what basis it makes its predictions. This process involved ranking over 55000 genes on the scale of their importance for examined cancer types. Finally, we were able to distinguish which ones are worth evaluating further. The scatter plot on the left shows the ones that we chose.",
                        style = {
                            'text-align': 'justify',
                            'text-justify': 'inter-word',
                            'padding-top':'20px',
                            'font-family': 'roboto-light',
                        }
                    )
                ],
                    style={'display': 'grid', 'grid-template-columns': '130px auto', 'grid-auto-flow': 'row'})
            ],
                style={'padding-left':'30px','padding-top':'40px'})
        ],
            style={'height':'500px','display': 'grid', 'grid-template-columns': '700px auto', 'grid-auto-flow': 'row',
                   'padding-top':'30px','padding-bottom':'50px'}
        ),
        html.Div([
            html.Div(),
            html.Div(style={'background-color': 'black', 'height': '1px'})
        ],
            style={'display': 'grid', 'grid-template-columns': 'auto 600px', 'grid-auto-flow': 'row', 'height': '1px'})
    ])

chapter_animation_description = \
    html.Div([
        html.Div([
            html.Div([
                html.H1("Exploring scientific context of discovery",
                        style={
                            'font-family': 'regularFont',
                            'font-size':'40px'}),
                html.Div([
                    html.Img(src='assets/arrow.jpg'),
                    html.P([
                        html.Span(
                            "We put the results of AI-based gene expression analysis into a context of available information obtained from the PubMed database. In order to give domain experts an easy way of gaining insights into scientific literature describing the correlations between certain genes and cancer types, we created a knowledge graph (on the left below). We retrieved, analyzed, and ranked over 10k scientific articles according to their importance and relevance to the topic."),
                        html.Br(),
                        html.Br(),
                        html.Span("How to read it? The lines describe the activation of genes in certain cancer types - color for indication, and thickness for value. The animation is showing the process of retrieving and analyzing publications. The result of this analysis is the establishing positions between nodes - close ones are closely related in the literature. Moreover, each line represents a top-1 article describing the correlation between two nodes eg. ‘Thyroid cancer’ and ‘TSHR’. By "),
                        html.Strong("clicking on nodes"),
                        html.Span(" you can access this paper. On the right side, we provide you a link to a publication as well as a "),
                        html.Strong("contextual chat bot"),
                        html.Span(" that will answer questions about the article.")
                    ],
                    style={
                        'text-align': 'justify',
                        'text-justify': 'inter-word',
                        'padding-top':'20px',
                        'font-family': 'roboto-light',
                    })
                ],
                    style={'display': 'grid', 'grid-template-columns': '130px auto', 'grid-auto-flow': 'row'})
            ]),
            html.Img(src='assets/genomic_analysis/stock-2.png',
                     style={'display': 'block'})
        ],
            style={'padding-top':'50px','padding-bottom':'50px',
                   'display': 'grid', 'grid-template-columns': '680px auto', 'grid-auto-flow': 'row'}
        ),
        html.Div([
            html.Div(style={'background-color': 'black', 'height': '1px'}),
            html.Div(style={'background-color': 'black', 'height': '1px'})
        ],
            style={'display': 'grid', 'grid-template-columns': '600px auto', 'grid-auto-flow': 'row', 'height': '1px'})
    ])

animation_and_chatbot = \
    html.Div([
        html.Div([
            # html.H1(
            #     'Click on the line between the two nodes and find the most relevant publications out of over 10k collected',
            #     style={
            #         'font-size': '13px',
            #         # 'padding-bottom':'10px'
            #     }),
            html.Div([
                html.Div([
                    html.H1("Examined publications: ",
                            style={
                                'font-size': '13px',
                                'padding-top': '6px'
                            }),
                    html.Div(
                        dbc.Progress(
                            id="progress_bar",
                            color="success",
                            animated=False,
                            style={"width": "390px", "height": "15px"},
                            striped=False
                        ),
                        style={
                            'padding-left': '12px',
                            'padding-right': '12px',
                            'padding-top': '6px'
                        }
                    ),
                    dbc.Button(
                        html.Img(src='assets/reload.png'),
                        id='reload-button',
                        n_clicks=0, color="link",
                        style={'margin-top':'-10px'}),
                ],
                    style={'display': 'grid',
                           'height': '32px',
                           'grid-template-columns': '140px 414px 70px',
                           'grid-auto-flow': 'row'}),
            ]),
            html.Div("", id='demo-info', style={'padding-left': '10px'}),
            html.Div([
                dcc.Graph(id='live-update-graph'),
                dcc.Store(id='graph-memory', storage_type='session'),
                dcc.Interval(
                    id='interval-component',
                    interval=1 * 850,  # in milliseconds
                    n_intervals=0,
                    max_intervals=200
                )
            ],
                id='relation-map',
                style={"width": "850px",
                       "display": "block",
                       'visibility': 'hidden',
                       "height": "600px",
                       'padding-top':'20px'}),
        ]),
        html.Div(),
        html.Div([
            html.Div([
                html.H1('Selected correlation of:',
                        style={
                            'font-size': '20px',
                            'color': 'black',
                            'font-weight': '400',
                            'display': 'inline-block',
                            'padding-right': '5px'
                        }),
                html.H1('Thyroid cancer',
                        style={
                            'font-size': '20px',
                            'color': 'rgba(227,0,15,1)',
                            'font-weight': '700',
                            'display': 'inline-block',
                            'padding-right': '5px'
                        },
                        id='selected-node-I'),
                html.H1('and',
                        style={
                            'font-size': '20px',
                            'color': 'rgba(227,0,15,1)',
                            'font-weight': '400',
                            'display': 'inline-block',
                            'padding-right': '5px'
                        }),
                html.H1('TSHR',
                        style={
                            'font-size': '20px',
                            'color': 'rgba(227,0,15,1)',
                            'font-weight': '700',
                            'display': 'inline-block'
                        },
                        id='selected-node-II'),
                html.Div()
            ],
                style={
                    'display': 'inline-block',
                    'grid-template-columns': 'auto auto auto auto auto',
                    'grid-auto-flow': 'row',
                    'padding-bottom': '5px'
                }),
            html.Div([
                html.Div("Chosen publication:",
                         style={'font-weight': 'bold'}),
                html.Div(),
                html.Div(
                    dbc.NavLink(
                        html.Div([
                            html.Img(src='assets/link.png'),
                            html.H1('Link to full article',
                                    style={'font-size': '12px',
                                           'font-weight': '400',
                                           'color': 'black',
                                           'padding-top': '4px',
                                           'text-decoration': 'none'})
                        ],
                            style={
                                'display': 'grid',
                                'grid-template-columns': '30px 100px',
                                'grid-auto-flow': 'row',
                            }),
                        href=r"https://www.europeanreview.org/wp/wp-content/uploads/4573-4580.pdf",
                        id="publication-link")
                )
            ],
                style={'display': 'grid',
                       'height': '32px',
                       'grid-template-columns': '240px auto 160px',
                       'grid-auto-flow': 'row'}),
            html.P(
                r"""Expression of sodium/iodide transporters and thyroid stimulating hormone receptors in
                thyroid cancer patients and its correlation with iodine nutrition status and pathology""",
                style={'font-style': 'italic',
                       'font-weight': '700',
                       'font-size': '16px',
                       'height': '60px',
                       'text-align': 'justify',
                       'text-justify': 'inter-character'
                       },
                id='publication-title'),
            dcc.Store(id='publication-text', storage_type='session'),
            # DIALOG BOX
            dcc.Store(data=json.dumps(dialog_history, indent=4), id='dialog-history'),
            html.Div([
                visdcc.Run_js(id='javascript'),
                html.Div([
                    *dialog(dialog_history)
                ],
                    style={"width": "624px",
                           "height": "485px",
                           "overflow-y": "auto",
                           "overflow-x": "hidden"},
                    className='custom-personal-scrollbar',
                    id='chat-bot-output'
                ),
                html.Div([
                    dcc.Input(id='user-query-input', value='Ask me a question...', type='text',
                              style={'border-radius': '15px', 'border': '1px solid rgba(227,0,15,0.1)',
                                     'padding-left': '10px', "box-shadow": "0px 0px 35px -12px rgba(227, 0, 17, 1)",
                                     'height': '40px'}),
                    html.Div(),
                    html.Button(
                        html.Div([
                            html.P("Submit",
                                   style={"color": "white", "font-size": "16px", "font-weight": "400",
                                          'padding-top': '6px', 'padding-right': '5px'}),
                            html.Img(src='assets/genomic_analysis/submit_arrow.png',
                                     style={'padding-bottom': '7px'}),
                        ],
                            style={'display': 'grid',
                                   'grid-template-columns': 'auto auto',
                                   'grid-auto-flow': 'row',
                                   'align-items': 'center',
                                   'justify-content': 'center'}),
                        id='user-query-button', n_clicks=0,
                        style={'height': '40px', 'background-color': 'rgba(227,0,17,1)',
                               'border-radius': '22px', 'border': '0px', "box-shadow": "0px 0px 35px -12px #E30011"})
                ],
                    style={'display': 'grid',
                           'grid-template-columns': '426px 20px 122px',
                           'grid-auto-flow': 'row',
                           "padding-left": "10px",
                           "padding-top": "10px",
                           }
                )
            ]),
            html.Div(id='hidden-div', style={'display': 'none'}),  # reference for callbacks with no output
        ])
    ],
    style={'display': 'grid',
           'grid-template-columns': f'624px auto 624px',
           'grid-auto-flow': 'row',
           'border-bottom':'solid black 1px',
           'padding-top':'50px','padding-bottom':'50px'})

chapter_summarization = \
    html.Div([
        html.Div([
            html.Div([
                html.H1("Knowledge base summarization",
                        style={
                            'font-family': 'regularFont',
                            'font-size':'40px'}),
                html.Div([
                    html.Img(src='assets/arrow.jpg'),
                    html.Div("To get insights on a higher, more general level we used all of the 10k retrieved publications as a context for summarization and answering more general questions. This is ‘How based on a given text gene expressions influence the development of thyroid cancer?’, ‘Is there described in the literature relation between proteins and ccRCC?’, and so on.",
                        style = {
                            'text-align': 'justify',
                            'text-justify': 'inter-word',
                            'padding-top':'20px',
                            'font-family': 'roboto-light',
                        }
                    )
                ],
                    style={'display': 'grid', 'grid-template-columns': '130px auto', 'grid-auto-flow': 'row'})
            ]),
            html.Div([
                dash_table.DataTable(data=table_data,
                                     columns=table_columns,
                                     id='table',
                                     style_cell={
                                         'textAlign': 'left',
                                     },
                                     style_data={
                                         'height': 'auto',
                                         'whiteSpace': 'pre-line',
                                    },
                                     css=[{
                                         'selector': '.dash-spreadsheet td div',
                                         'rule': '''width: 1000px''',
                                     }],
                                     ),
            ],
                style={'width': '850px',
                       'padding-left':'50px',
                       'margin': 'auto'},
                id='specification-table')
        ],
            style={'padding-top':'50px','padding-bottom':'50px',
                   'display': 'grid', 'grid-template-columns': '450px auto', 'grid-auto-flow': 'row'}
        ),
        html.Div([
            html.Div(style={'background-color': 'black', 'height': '1px'}),
            html.Div()
        ],
            style={'display': 'grid', 'grid-template-columns': '650px auto', 'grid-auto-flow': 'row', 'height': '1px'})
    ])


chapter_results = \
    html.Div([
        html.H1("Results & generalization to future studies",
                        style={
                            'font-family': 'regularFont',
                            'font-size':'40px'}),
        html.Div([
            html.Img(src='assets/arrow.jpg'),
            html.P([
                html.Span("The study gave us positive results. We were able to find the most important genes for cancer development. Furthermore, we found that the literature suggests such implications of those genes. The interactive graph and contextual chatbot gave our domain expert the opportunity to dive deeper into the subject and go through a significantly larger amount of articles in a quicker way."),
                html.Br(),
                html.Br(),
                html.Span("The discovery has a few major implications. It enables radically faster examination of cancer predisposition by testing only several gene expressions rather than previously 55 thousand ones. It focuses our future research on the experiments on the most important genes. Part of this article's motivation was an exemplification of a new standard of cooperation between data scientists and domain experts enabled by the usage of large language models like ChatGPT."),
                html.Br(),
                html.Br(),
                html.Strong("What problems did we solve that can be applied to other projects?"),
                html.Br(),
                html.Span("- Extensive analysis of predictive models"),
                html.Br(),
                html.Span("- Solving classification a problem with an extremely small patient sample size (~500 patients with 55k gene records)"),
                html.Br(),
                html.Span("- Explainability of model decisions"),
                html.Br(),
                html.Span("- Scientific information retrieval from online publication databases"),
                html.Br(),
                html.Span("- Processing of large amounts of complex text - summarization"),
                html.Br(),
                html.Span("- Creating chatbot with its own knowledge base"),
                html.Br(),
                html.Span("- Creating advanced graphs for the representation of complex correlations within the data"),
            ],
                style={
                    'text-align': 'justify',
                    'text-justify': 'inter-word',
                    'border-bottom': 'solid black 1px',
                    'margin-right':'150px',
                    'padding-top':'20px','padding-bottom':'50px',
                    'font-family': 'roboto-light',
                }
            )
        ],
            style={'display': 'grid', 'grid-template-columns': '130px auto', 'grid-auto-flow': 'row'})
    ],
    style={'padding-top': '50px', 'display': 'grid'}
    )

chapter_publication = \
    html.Div([
        html.Div(),
        html.Img(src='assets/genomic_analysis/logo.png',style={'width':'350px'}),
        html.Div(),
        html.Div([
            html.H1("Our publication", style={'width':'350px',
                                              'font-family': 'ultraboldFont',
                                              'font-size': '40px',
                                              'font-weight': '600'
                                              }),
            html.Div([
                html.Img(src='assets/arrow.jpg'),
                dbc.NavLink(
                    html.Div([
                        html.H1('Read our article ',
                                style={'font-size': '16px',
                                       'font-weight': '400',
                                       'color': 'black',
                                       'text-decoration': 'none',
                                       'font-family': 'roboto-light'}),
                        html.Img(src='assets/link.png'),
                    ],
                        style={
                            'display': 'grid',
                            'grid-template-columns': '130px 50px',
                            'grid-auto-flow': 'row'
                        }),
                    href=r"https://drive.google.com/file/d/11L4PlsyDZCCB3I-MuzUvzYf9w9hRajxz/view?usp=sharing",
                style={'padding-top':'65px'}),
            ],
                style={'display': 'grid', 'grid-template-columns': '130px auto', 'grid-auto-flow': 'row'})
        ],style={'padding-top':'80px'}),
        html.Div(),
        html.Div()
    ],
        style={'padding-top':'50px',
               'display': 'grid', 'grid-template-columns': 'auto 350px 120px 270px 80px auto', 'grid-auto-flow': 'row'}
    )

layout = \
    portfolio_wrapper(
        chapter_headline,
        chapter_models,
        chapter_genes,
        chapter_animation_description,
        animation_and_chatbot,
        chapter_summarization,
        chapter_results,
        chapter_publication
    )