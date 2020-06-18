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
    [
        html.H1("Cohort dashboard"),
        html.Div("View individual's progress below."),
        dcc.Graph(
            id="cohort-progress",
            figure={
                "data": [
                    {
                        "x": ["tom", "kevin", "thibaud", "tolu"],
                        "y": [10, 5, 2, 15],
                        "type": "bar",
                        "name": "participants",
                    },
                ],
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
