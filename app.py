import panel as pn
import pandas as pd

# Initialize Panel
pn.extension()

# Define input widgets
name_input = pn.widgets.TextInput(name='Name')
age_input = pn.widgets.IntInput(name='Age', step=1, start=0, end=120)
gender_input = pn.widgets.Select(name='Gender', options=['Male', 'Female', 'Other'])

# Submit button
submit_button = pn.widgets.Button(name='Submit', button_type='primary')

# Message area
message_area = pn.pane.Markdown('')

# Define the file name
csv_file = 'user_inputs.csv'

# Function to save input to CSV
def save_to_csv(event):
    data = {
        'Name': [name_input.value],
        'Age': [age_input.value],
        'Gender': [gender_input.value]
    }
    df = pd.DataFrame(data)
    
    try:
        # Append data to CSV or create a new file if it doesn't exist
        if not pd.io.common.file_exists(csv_file):
            df.to_csv(csv_file, index=False)
        else:
            df.to_csv(csv_file, mode='a', header=False, index=False)
        
        # Clear inputs and show success message
        name_input.value = ''
        age_input.value = None
        gender_input.value = 'Male'
        message_area.object = "**Success! Data has been saved.**"
    except Exception as e:
        message_area.object = f"**Error saving data: {e}**"

# Link button click to save function
submit_button.on_click(save_to_csv)

# Layout
app_layout = pn.Column(
    "# User Input Form",
    name_input,
    age_input,
    gender_input,
    submit_button,
    message_area
)

# Serve the app
app_layout.servable()
