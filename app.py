import panel as pn
import pandas as pd
import calculations as c

pn.extension()

# Function to process questionnaire responses
def process_questionnaire(event):
    # Save responses to a CSV file
    responses = {key: value for key, value in inputs.items()}
    df_responses = pd.DataFrame([responses])
    df_responses.to_csv("responses.csv", index=False)

def your_calculation_function(resposta):
    


    # Run calculations (imported from your script)
    results = c.your_calculation_function(df_responses)  # Replace with your actual function

    # Save results to an Excel file
    results.to_excel("results.xlsx", index=False)

    # Provide a download link for the results
    download_button.filename = "results.xlsx"
    download_button.file = "results.xlsx"

# Define inputs
inputs = {
    "Question 1": pn.widgets.IntInput(name="Enter your response for Question 1"),
    "Question 2": pn.widgets.IntInput(name="Enter a number for Question 2"),
    # Add more inputs as needed
}

# Add a submit button
submit_button = pn.widgets.Button(name="Submit", button_type="primary")
submit_button.on_click(process_questionnaire)

# Add a download button
download_button = pn.widgets.FileDownload(button_type="success", disabled=True)

# Layout
dashboard = pn.Column(
    pn.pane.Markdown("# Questionnaire"),
    *inputs.values(),
    submit_button,
    download_button
)

if __name__ == "__main__":
    dashboard.servable()
