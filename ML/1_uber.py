# !pip install geopy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from geopy.distance import geodesic

df = pd.read_csv("1_uber.csv")
df.head()

df.shape
print(df.info())

# Convert 'pickup_datetime' to datetime
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

# Drop rows with missing values in 'pickup_datetime' and 'fare_amount'
df.dropna(subset=['pickup_datetime', 'fare_amount'], inplace=True)

# Remove negative and extremely high values in 'fare_amount' and 'passenger_count'
df = df[(df['fare_amount'] > 0) & (df['fare_amount'] < 100)]
df = df[(df['passenger_count'] > 0) & (df['passenger_count'] <= 6)]

df.shape

# Extract date and time features from 'pickup_datetime'
df['pickup_hour'] = df['pickup_datetime'].dt.hour
df['pickup_day'] = df['pickup_datetime'].dt.day
df['pickup_month'] = df['pickup_datetime'].dt.month
df['pickup_year'] = df['pickup_datetime'].dt.year

print(df[['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude']].isnull().sum())

# Filter out rows with invalid latitude or longitude
df = df[(df['pickup_latitude'].between(-90, 90)) & 
        (df['pickup_longitude'].between(-180, 180)) &
        (df['dropoff_latitude'].between(-90, 90)) &
        (df['dropoff_longitude'].between(-180, 180))]

df.head()
df.shape

# Setting up the figure for four box plots
plt.figure(figsize=(12, 8))

# Plotting box plots for each of the four columns
columns = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']
for i, col in enumerate(columns, 1):
    plt.subplot(2, 2, i)  # 2 rows, 2 columns layout
    sns.boxplot(y=df[col])
    plt.title(f'Box plot of {col}')

plt.tight_layout()
plt.show()

def calculate_distance(row):
    try:
        return geodesic(
            (row['pickup_latitude'], row['pickup_longitude']),
            (row['dropoff_latitude'], row['dropoff_longitude'])
        ).km
    except ValueError as e:
        print(f"Error calculating distance for row {row.name}: {e}")
        return None  # or 0, depending on how you want to handle errors

df['distance_km'] = df.apply(calculate_distance, axis=1)

df = df[df['distance_km'] > 0]
df = df[df['distance_km'] < 100]

# Detect outliers using the IQR method
outliers = pd.DataFrame()  # To store outliers for each column
columns_to_check = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']

# Apply the IQR method for each column to identify outliers
for col in columns_to_check:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter rows that are outliers in this column
    col_outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outliers = pd.concat([outliers, col_outliers])

# Remove duplicate rows (as some rows may be outliers in multiple columns)
outliers = outliers.drop_duplicates()

# Remove detected outliers from the original DataFrame
df_no_outliers = df[~df.index.isin(outliers.index)]

# Display the number of rows before and after removing outliers
print("Original number of rows:", len(df))
print("Number of rows after removing outliers:", len(df_no_outliers))

df = df_no_outliers.copy()

# Setting up the figure for four box plots
plt.figure(figsize=(12, 8))

# Plotting box plots for each of the four columns
columns = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']
for i, col in enumerate(columns, 1):
    plt.subplot(2, 2, i)  # 2 rows, 2 columns layout
    sns.boxplot(y=df[col])
    plt.title(f'Box plot of {col}')

plt.tight_layout()
plt.show()

df.shape
df.drop(['key', 'pickup_datetime', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude'], axis=1, inplace=True)
df

plt.scatter(df["distance_km"], df["fare_amount"])
plt.xlabel("Distance")
plt.ylabel("Fare Amount")
plt.show()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# 4. Implement Linear Regression and Random Forest Regression models
# Define features and target variable
X = df.drop('fare_amount', axis=1)
y = df['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Initialize and train the Random Forest Regression model
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest_model.fit(X_train, y_train)

# Predict on test set
y_pred_linear = linear_model.predict(X_test)
y_pred_rf = random_forest_model.predict(X_test)

# Calculate evaluation metrics
def evaluate_model(y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return r2, rmse

# Linear Regression evaluation
r2_linear, rmse_linear = evaluate_model(y_test, y_pred_linear)
print("Linear Regression:")
print(f"R^2 Score: {r2_linear:.4f}")
print(f"RMSE: {rmse_linear:.4f}")

# Random Forest Regression evaluation
r2_rf, rmse_rf = evaluate_model(y_test, y_pred_rf)
print("\nRandom Forest Regression:")
print(f"R^2 Score: {r2_rf:.4f}")
print(f"RMSE: {rmse_rf:.4f}")

# plot
plt.figure(figsize=(17, 5))

# Linear Regression Predictions
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_linear, alpha=0.5, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Fare")
plt.ylabel("Predicted Fare")
plt.title("Linear Regression: Actual vs Predicted Fares")

# Adjust axis limits to zoom in
plt.xlim([y_test.min()+5, y_test.max()])
plt.ylim([y_pred_linear.min()+3, y_pred_linear.max()+3])

# Random Forest Predictions
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_rf, alpha=0.5, color='green')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Fare")
plt.ylabel("Predicted Fare")
plt.title("Random Forest: Actual vs Predicted Fares")

# Adjust axis limits to zoom in
plt.xlim([y_test.min()+5, y_test.max()])
plt.ylim([y_pred_rf.min()+3, y_pred_rf.max()+3])

plt.show()




