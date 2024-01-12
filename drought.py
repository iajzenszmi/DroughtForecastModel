import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv('drought_forecast_data.csv')

# Preprocess the data
# (e.g., handling missing values, feature scaling, etc.)

# Select relevant features
X = data[['rainfall', 'temperature', 'humidity']]  # Example features
y = data['drought_status']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")

# Use the model for forecasting
# forecast = model.predict(new_data)
