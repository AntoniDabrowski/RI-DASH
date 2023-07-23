"""
    The following code is under CC-BY-NC-SA 4.0 license (more in root/LICENSE.txt)
            Free to use and redistribute for any non-commercial purpose
"""

from dash import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import os
import openai
from dotenv import load_dotenv
import dash
import json

from utils.pages.genomic_analysis.database_handling import context_chatbot
from utils.pages.genomic_analysis.utils import dialog, dialog_history as initial_dialog_history

load_dotenv('.env')

if not os.environ.get('OPENAI_API_KEY'):
    raise ValueError("You have to provide valid OpenAI API key in '.env' file in the root of the repository.")
openai.api_key = os.environ['OPENAI_API_KEY']

@dash.callback(
    [Output('chat-bot-output', 'children'), Output('user-query-input', 'value'),Output('dialog-history','data'),Output('javascript', 'run')],
    Input('user-query-button', 'n_clicks'),
    [State('user-query-input', 'value'), State('publication-text', 'data'), State('selected-node-I','children'),
     State('selected-node-II','children'),State('dialog-history','data')]
)
def update_output_chat_bot(n_clicks, user_message, context,first_node,second_node,dialog_history_json):
    if n_clicks > 0:
        if not context:
            context = 'publications/TXTs/000010.txt'
        bot_message = context_chatbot(context).query(user_message).lstrip()
        dialog_history = json.loads(dialog_history_json) if dialog_history_json else initial_dialog_history
        current_message_id = len(dialog_history) // 2
        dialog_history[f'user-{current_message_id}'] = [user_message,first_node,second_node]
        dialog_history[f'bot-{current_message_id+0.1}'] = bot_message
        return dialog(dialog_history), "Ask me a question...", json.dumps(dialog_history, indent=4), \
            "var objDiv = document.getElementById('chat-bot-output');objDiv.scrollTop = objDiv.scrollHeight;"
    raise PreventUpdate

@dash.callback(
    [Output('publication-title', 'children'), Output('publication-link', 'href'),
     Output('publication-text', 'data'),Output('selected-node-I','children'),Output('selected-node-II','children')],
    Input('live-update-graph', 'clickData'))
def update_publication_title(clickData):
    if clickData and "customdata" in clickData["points"][0] and clickData["points"][0]["customdata"]:
        if len(clickData['points'][0]['customdata'][0]) <= 7:
            raise PreventUpdate
        text = clickData['points'][0]['customdata'][0][7:]
        if text[0] != '(':
            raise PreventUpdate
        text = eval(text)
        title, url = text

        file_name,first_cancer_type,second_cancer_type = get_publication_context(url)

        return title, url, file_name, first_cancer_type, second_cancer_type
    raise PreventUpdate

def get_publication_context(url):
    path = 'data/genomic_analysis/publications.csv'
    df = pd.read_csv(path)
    file_name = df[df['url'] == url]['file_name'].values[0]
    first_cancer_type = df[df['url'] == url]['first_cancer_type'].values[0]
    second_cancer_type = df[df['url'] == url]['second_cancer_type'].values[0]
    return f'./publications/TXTs/{file_name}',first_cancer_type,second_cancer_type