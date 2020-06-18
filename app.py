import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# Initialise dash app
app = dash.Dash()

COLOURS = {
    "red": "#d92027",
    "orange": "#ff9234",
    "yellow": "#ffcd3c",
    "green": "#35d0ba",
    "pale": "#ddf3f5",
    "dark": "#393e46",
}

colours = {
    "background": COLOURS["dark"],
    "text": COLOURS["pale"],
}

app.layout = html.Div(
    children=[
        html.H1(children="Cohort dashboard"),
        html.Div(
            children="""
                View individual's progress below.
            """
        ),
        dcc.Graph(
            id="cohort-progress",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [10, 5, 2], "type": "bar", "name": "Tom"},
                    {"x": [1, 3, 5], "y": [10, 5, 2], "type": "bar", "name": "Kevin"},
                    {"x": [1, 2, 5], "y": [4, 20, 2], "type": "bar", "name": "Thibaud"},
                ]
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
