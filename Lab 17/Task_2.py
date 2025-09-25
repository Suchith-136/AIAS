import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('financial_data.csv')

# Handle missing values in 'closing_price' and 'volume'
# For example, fill missing values with the mean of each column
df['closing_price'] = df['closing_price'].fillna(df['closing_price'].mean())
df['volume'] = df['volume'].fillna(df['volume'].mean())

# Save the cleaned data (optional)
# Create lag features: 1-day and 7-day returns
df['return_1d'] = df['closing_price'].pct_change(periods=1)
df['return_7d'] = df['closing_price'].pct_change(periods=7)

# Save the cleaned data with lag features
# Normalize 'volume' column using log-scaling
df['volume_log'] = np.log1p(df['volume'])

# Detect outliers in 'closing_price' using the IQR method
Q1 = df['closing_price'].quantile(0.25)
Q3 = df['closing_price'].quantile(0.75)
IQR = Q3 - Q1
outlier_mask = (df['closing_price'] < (Q1 - 1.5 * IQR)) | (df['closing_price'] > (Q3 + 1.5 * IQR))
df['closing_price_outlier'] = outlier_mask

df.to_csv('financial_data_cleaned.csv', index=False)