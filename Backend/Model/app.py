from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model and encoders
model = joblib.load('bail_prediction_model.pkl')
section_encoder = joblib.load('section_encoder.pkl')
bailable_encoder = joblib.load('bailable_encoder.pkl')

# Route to serve the HTML page
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# API endpoint for prediction
@app.route('/predict-bail/', methods=['POST'])
def predict_bail():
    # Get the IPC section from the POST request
    data = request.get_json()
    ipc_section = data.get('ipc_section')

    # Ensure that the IPC section is valid
    if ipc_section not in section_encoder.classes_:
        return jsonify({'bail_status': 'Unknown IPC Section'})

    # Encode the IPC section
    ipc_section_encoded = section_encoder.transform([ipc_section])[0]

    # Create DataFrame for the input
    input_data = pd.DataFrame([[ipc_section_encoded]], columns=['IPC Section'])

    # Make prediction
    prediction = model.predict(input_data)
    bail_status = bailable_encoder.inverse_transform(prediction)[0]

    # Return the result as JSON
    return jsonify({'bail_status': bail_status})

if __name__ == '__main__':
    app.run(debug=True)
