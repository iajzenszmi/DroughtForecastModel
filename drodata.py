import pandas as pd
import numpy as np

# Creating a sample dataset
np.random.seed(0)
data = {
    "date": pd.date_range(start="2020-01-01", periods=100, freq='D'),
    "rainfall": np.random.uniform(0, 100, 100),  # Random values between 0 and 100
    "temperature": np.random.uniform(20, 35, 100),  # Random values between 20°C and 35°C
    "humidity": np.random.uniform(30, 90, 100),  # Random values between 30% and 90%
    "drought_status": np.random.choice([0, 1], 100)  # 0 for no drought, 1 for drought
}

df = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
csv_file = 'drought_forecast_data.csv'
df.to_csv(csv_file, index=False)

csv_file
