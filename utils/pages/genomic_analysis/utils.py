"""
    The following code is under CC-BY-NC-SA 4.0 license (more in root/LICENSE.txt)
            Free to use and redistribute for any non-commercial purpose
"""

from dash import html
import pandas as pd

table_df_path = './data/genomic_analysis/table_content_short.pickle'

table_df = pd.read_pickle(table_df_path)
table_data = [{"type": "Genes", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Genes"],
               "ccRCC": table_df.loc["ccRCC"]["Genes"]},
              {"type": "Proteins", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Proteins"],
               "ccRCC": table_df.loc["ccRCC"]["Proteins"]},
              {"type": "Lipids/fats", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Lipids/fats"],
               "ccRCC": table_df.loc["ccRCC"]["Lipids/fats"]},
              {"type": "Metabolites", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Metabolites"],
               "ccRCC": table_df.loc["ccRCC"]["Metabolites"]}]
table_columns = [{"name": "", "id": "type"}, {"name": "Thyroid Carcinoma", "id": "Thyroid_Carcinoma"},
                 {"name": "ccRCC", "id": "ccRCC"}]

table_description = \
    """The table below shows key insights on a given topic based on analysis of over 10k publications collected from 
    online repository OpenAlex. The analysis was performed by our specialized information retrieval system.
    It ranked the most important elements for a given topic and provided the most relevant publications.
    Then, the system created semantic embeddings of paragraphs and used them to answer question about the relation
    between two topics. The table below shows the most important elements for two types of cancer."""



plot_description = \
    """The visualization above shows key insights from our study in the
    context of scientific literature. Precisely it describes the relationship between two types of cancers
    and their most discriminating genes. Our analysis showed not only that exactly those eight genes are
    most influential for prediction but also what is their activation in a certain type of disease - color
    for indication and thickness for value. The establishing distances between nodes shows how closely related
    are they based in indications from collected scientific literature."""

plot_instruction = \
    """Click on the line between the two nodes and find the most relevant publications out of over 10k collected."""

chatbot_description = \
    """The chatbot above is a tool that can help you to find answers to your questions about the study.
    It is based on the OpenAI ChatGPT model and it is applied via elastic search algorithm to retrieve information about
    the scientific literature that we collected. It is also possible to ask it about the meaning of the terms that 
    are used in the publication. The chatbot is still in the development phase, so it may not be able to answer all your 
    questions."""

dialog_history = {
    'user-0':['What are the results of the given study?','ccRCC','HOXB7'],
    'bot-0.1':'The results of the study showed that the expression of NIS and TSHR protein was significantly reduced in the thyroid cancer group compared with the normal group.',
    'user-1':['Tell me more about expression of NIS and TSHR protein','ccRCC','HOXB7'],
    'bot-1.1':'Western blotting results showed that the expression of NIS and TSHR protein was significantly reduced in the thyroid cancer group compared with the normal group. Immunohistochemistry showed the positive expression of NIS and TSHR in thyroid cancer group. The expression of NIS and TSHR mRNA and protein in thyroid cancer patients was significantly lower than that in normal group detected by RT-PCR and Western blotting.',
}

def process_message(message):
    final = []
    for a in message.split('\n'):
        final.append(html.H1(a,style={'font-weight': '400', 'font-size': '16px'}))
    return html.Span(final)
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
        html.Div(
            html.Div(process_message(message),
                     style={'background-color': 'rgba(227,0,15,0.1)',
                            'padding': '10px', 'border-radius': '15px', "border-top-left-radius": "0px",
                            'display':'inline-block'}),
            style={'width':'480px'}
        ),
    ],
        style={'width': '100%', 'align-items': 'right', 'justify-content': 'right', 'display': 'grid',
               'padding-right': '64px', 'grid-auto-flow': 'row',
               'grid-template-columns': '48px 7px auto','padding-bottom':'30px'})

def dialog(json_history):
    messages = {}
    for key in json_history:
        if key.startswith('user'):
            messages[float(key.split('-')[1])] = \
                user_message_generator(*json_history[key])
        elif key.startswith('bot'):
            messages[float(key.split('-')[1])+0.1] = \
                bot_message_generator(json_history[key])
        else:
            raise ValueError('Invalid key in json_history')
    return list(map(lambda kv: kv[1], sorted(messages.items())))