import numpy as np
import pandas as pd
from model import DDoSModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the CSV data
data = pd.read_csv('Monday-WorkingHours.pcap_ISCX.csv')
data.columns = [column.strip() for column in data.columns]

# Ensure the 'Label' column exists and drop rows with NaN values
if 'Label' in data.columns:
    data.dropna(subset=['Label'], inplace=True)
else:
    raise KeyError("The 'Label' column is not found in the dataset.")

# Split data into features and labels
X = data.drop(columns=['Label'])
y = data['Label']

# Convert all columns to numeric and handle errors
X = X.apply(pd.to_numeric, errors='coerce')

# Replace inf values with NaN and then drop rows with NaN values
X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.dropna(inplace=True)

# Align y with X to ensure consistent lengths
y = y[X.index]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = DDoSModel()
model.train(X_train, y_train)

# Save the model
model.save_model('ddos_model.pkl')

# Load the model and make predictions on the test set
model.load_model('ddos_model.pkl')
predictions = model.predict(X_test)

# Print the predictions
print(predictions)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')
print(classification_report(y_test, predictions))
