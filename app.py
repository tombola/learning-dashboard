import dash
import dash_core_components as dcc
import dash_html_components as html

# Initialise dash app
app = dash.Dash()

COLOURS = {
    "red": "#d92027",
    "orange": "#ff9234",
    "yellow": "#ffcd3c",
    "green": "#35d0ba",
}

TONES = {
    "pale": "#ddf3f5",
    "dark": "#393e46",
}

PARTICIPANTS_PROGRESS = {
    "tom": 10,
    "kevin": 5,
    "thibaud": 2,
    "tolu": 15,
}


def get_participant_names():
    # ["tom", "kevin", "thibaud", "tolu"]
    return list(PARTICIPANTS_PROGRESS.keys())


def get_participant_progress_values():
    # [10, 5, 2, 15]
    return [PARTICIPANTS_PROGRESS[n] for n in get_participant_names()]


intro = """
# Cohort dashboard

View individual participants progress below.
"""


app.layout = html.Div(
    [
        dcc.Markdown(intro),
        dcc.Graph(
            id="cohort-progress",
            figure={
                "data": [
                    {
                        "x": get_participant_names(),
                        "y": get_participant_progress_values(),
                        "type": "bar",
                        "name": "participants",
                        "marker": {"color": [COLOURS[c] for c in COLOURS.keys()]},
                    },
                ],
                "layout": {
                    "yaxis": {
                        "title": {
                            "text": "Tutorial Stage",
                            # "standoff": 60,
                            # "font": {"size": 25},
                        },
                        "automargin": True,
                        # "showline": True,
                        # "mirror": True,
                    },
                },
            },
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
