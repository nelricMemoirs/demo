import dash
import dash_bootstrap_components as dbc
import dash
import dash_bootstrap_components as dbc
from dash import html
from processing.custom import read_dataset, ambil_sebagian_kolom
from processing.processsing import process_nan, transform_log
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# read dataset adn processing
path = 'sample data.csv'
df = read_dataset(path) 
fig = px.box(df.loc[:, 'P_2':'D_41'])

processed_df = ambil_sebagian_kolom(df, ['P_2','D_41'])
processed_df = process_nan(processed_df)
processed_df = transform_log(processed_df)
after_fig = px.box(processed_df)


hist_fig = make_subplots(rows=3, cols=3)

row = 1
col = 1
for x in (processed_df.columns):
    if col > 3 :
        col = 1
        row += 1

    hist_fig.add_trace(
        go.Histogram(x=processed_df[x], nbinsx=30, name=x),
        row=row, col=col, 
    )

    col += 1




# =============================================================================
# ===================== MAIN APP ==============================================
# =============================================================================
dash_app = dash.Dash(__name__, suppress_callback_exceptions=True,
                    requests_pathname_prefix='/dashboard/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP])

left_jumbotron = dbc.Col(
    html.Div(
        [
            html.H2("Before Data Transformation", className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                "This dataset has been filtered for selected columns only without any processing."
            ),
            dbc.Button("See details", color="light", outline=True),
        ],
        className="h-100 p-5 text-white bg-dark rounded-3",
    ),
    md=6,
)

right_jumbotron = dbc.Col(
    html.Div(
        [
            html.H2("After Data Transformation", className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                "This dataset already transformed and processed using log transform"
            ),
            dbc.Button("See details", color="secondary", outline=True),
        ],
        className="h-100 p-5 bg-light border rounded-3",
    ),
    md=6,
)

jumbotron = dbc.Row(
    [left_jumbotron, right_jumbotron],
    className="align-items-md-stretch",
)

before_boxplot = dbc.Col(
    html.Div(children=[
    
    html.H3("Before"),
    
    dash.dcc.Graph(id="before", figure=fig)
    
    ]),
    md=6
)

after_boxplot = dbc.Col(
    html.Div(children=[
    
    html.H3("After"),
    
    dash.dcc.Graph(id="after", figure=after_fig)
    
    ]
    ),
    md=6
)


dist_plot = html.Div(children=[
    
    dash.dcc.Graph(id="hist", figure=hist_fig)
    
    ], style = {'width': '40%'})
    

boxplot = dbc.Row(
    [before_boxplot, after_boxplot],
    className="align-items-md-stretch",
)






dash_app.layout = html.Div(children=[
    jumbotron,
    boxplot,
    dist_plot
])
