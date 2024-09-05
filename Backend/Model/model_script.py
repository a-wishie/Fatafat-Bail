import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
import joblib

# Load the dataset
data = pd.read_csv('IPC112.csv')

# Strip any leading/trailing whitespace from column names
data.columns = data.columns.str.strip()

# Handle special case for 'Depends on the offense'
data['Bailable'] = data['Bailable'].apply(lambda x: 'No' if 'No' in x else 'Yes')

# Encode the 'Bailable' column to numerical values
bailable_encoder = LabelEncoder()
data['Bailable'] = bailable_encoder.fit_transform(data['Bailable'])

# Encode the 'IPC Section' column
section_encoder = LabelEncoder()
data['IPC Section'] = section_encoder.fit_transform(data['IPC Section'])

# Define features and target variable
X = data[['IPC Section']]
y = data['Bailable']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Handle imbalanced data using SMOTE
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Initialize the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train_res, y_train_res)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred, target_names=bailable_encoder.classes_))

# Save the model for future use
joblib.dump(model, 'bail_prediction_model.pkl')
joblib.dump(section_encoder, 'section_encoder.pkl')
joblib.dump(bailable_encoder, 'bailable_encoder.pkl')

# Function to predict bail based on IPC section
def predict_bail(ipc_section):
    # Load the trained model
    model = joblib.load('bail_prediction_model.pkl')
    
    # Encode the input feature
    if ipc_section not in section_encoder.classes_:
        return "Unknown IPC Section"
    
    ipc_section_encoded = section_encoder.transform([ipc_section])[0]
    
    # Create a DataFrame for the input
    input_data = pd.DataFrame([[ipc_section_encoded]], columns=['IPC Section'])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Decode the prediction
    bail_status = bailable_encoder.inverse_transform(prediction)[0]
    
    return bail_status

# Example usage
ipc_section = input("enter section: ")
bail_status = predict_bail(ipc_section)
print(f'Bail Status: {bail_status}')