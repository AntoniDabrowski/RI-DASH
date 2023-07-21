import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


# @dash.callback(Output("company-button-id", "style"),
#                Input('company-button-id', 'hoverInfo'))
# def hover_company(hover):
#     print(hover)
#     if hover:
#         return {'font-size':'16px',
#                 'font-weight': 'bold'}
#     return {'font-size':'16px'}
