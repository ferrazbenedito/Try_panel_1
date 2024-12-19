import panel as pn
import pandas as pd
import os

# Initialize Panel extension
pn.extension()

# Define the questions
questions = [
    ("What is your name?", "name"),
    ("What is your age?", "age"),
    ("What is your favorite color?", "favorite_color"),
    ("What is your favorite hobby?", "hobby"),
    ("Where do you live?", "location"),
]

# Create input widgets for each question
inputs = {key: pn.widgets.TextInput(name=question) for question, key in questions}

# File to store responses
csv_file = "responses.csv"

# Save responses to CSV
def save_responses(event):
    response_data = {key: widget.value for key, widget in inputs.items()}
    df = pd.DataFrame([response_data])

    # Check if the file exists, append if it does
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, index=False)

    # Show success message
    status_pane.object = "Responses saved successfully!"

# Create a submit button
submit_button = pn.widgets.Button(name="Submit", button_type="primary")
submit_button.on_click(save_responses)

# Create a status pane to display messages
status_pane = pn.pane.Markdown("", style={'color': 'green'})

# Layout the form
form = pn.Column(
    pn.pane.Markdown("## Answer the questions below:"),
    *[inputs[key] for key in inputs],
    submit_button,
    status_pane,
)

# Serve the app
app = pn.template.FastListTemplate(
    title="Simple Survey App",
    main=[form],
)

# Run this to serve locally
def serve():
    app.show()

# For deployment to Heroku
def panel_serve():
    return app
