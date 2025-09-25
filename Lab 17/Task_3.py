import pandas as pd

# Read the CSV file
df = pd.read_csv('iot_sensor.csv')

# Forward fill missing values
df_filled = df.fillna(method='ffill')


# Apply rolling mean to 'temperature' and 'humidity' columns to smooth data
df_filled['temperature'] = df_filled['temperature'].rolling(window=5, min_periods=1).mean()
df_filled['humidity'] = df_filled['humidity'].rolling(window=5, min_periods=1).mean()

# Save the result to a new CSV file (optional)
# Normalize 'temperature' and 'humidity' columns using standard scaling
for col in ['temperature', 'humidity']:
    mean = df_filled[col].mean()
    std = df_filled[col].std()
    df_filled[col] = (df_filled[col] - mean) / std

# Encode categorical sensor IDs
df_filled['sensor_id'] = df_filled['sensor_id'].astype('category').cat.codes

df_filled.to_csv('iot_sensor_filled_new.csv', index=False)

# Print the filled DataFrame
print(df_filled)