"""
This file demonstrates the creation of a simple tree in dash
"""
import dash
from dash import dcc
import dash.html as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# def aggrid_example(app):
#     columnDefs = [
#         {"headerName": "Make", "field": "make"},
#         {"headerName": "Model", "field": "model"},
#         {"headerName": "Price", "field": "price"},
#     ]

#     rowData = [
#         {"make": "Toyota", "model": "Celica", "price": 35000},
#         {"make": "Ford", "model": "Mondeo", "price": 32000},
#         {"make": "Porsche", "model": "Boxter", "price": 72000},
#     ]


#     app.layout = ddk.Row(
#         [
#             dag.AgGrid(
#                 id="ag-grid",
#                 columnDefs=columnDefs,
#                 rowData=rowData,
#                 columnSize="sizeToFit",
#                 defaultColDef=dict(
#                     resizable=True,
#                 ),
#             ),
#         ]
#     )

def hello_world_example(app):
    app.layout = html.Div(children=[
        html.H1("Hello World"),
        html.P("This is the first application. Yo")
    ])

if __name__=="__main__":
    aggrid_example(app)
    app.run_server(debug=True)