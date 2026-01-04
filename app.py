from dash import Dash, callback, Input, Output
from Layouts.layout import (create_layout, create_overall_analysis_content,
                            create_cancellations_content, create_ratings_content,
                            create_raw_data_content)
from Callbacks.callbacks import register_callbacks

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server
app.title = "Uber Dashboard"

app.layout = create_layout()

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/cancellations":
        return create_cancellations_content()
    elif pathname == "/ratings":
        return create_ratings_content()
    elif pathname == "/raw-data":
        return create_raw_data_content()
    else:
        return create_overall_analysis_content()

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)