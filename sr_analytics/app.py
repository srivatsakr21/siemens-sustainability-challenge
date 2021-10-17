import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import base64


app = dash.Dash(__name__)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
image_filename = 'Overview.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
image_filename_2 = 'ms_response.png' # replace with your own image
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read())

app.layout = html.Div(
    children=[
        html.Div(
            children = [html.H1(children="SustainaBits Analytics",className="header-title"),
            html.P(
                children="Analyze Your CSR reports"
                " and get insights on public perception of your action"
            ,   className="header-description"
            )], className="header"
        ),
        
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style={
                'height': '50%',
                'width': '50%'
            }),
        
    ], style={'textAlign': 'center'}
)

if __name__ == "__main__":
    app.run_server(debug=True)