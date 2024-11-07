import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("5_sales_data_sample.csv", encoding='ISO-8859-1')
df
df.shape
print(df.info())

# Dropping unnecessary columns for clustering (ORDERNUMBER, ORDERDATE, etc.)
df = df[['QUANTITYORDERED', 'PRICEEACH', 'SALES']]
df.dropna()

# Check for any null values
print("Null values:\n", df.isnull().sum())

# Scaling data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Model
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 3: Determine the optimal number of clusters using the Elbow Method
# The elbow point in the curve suggests the best value for K (number of clusters). 
# It's where the inertia stops decreasing significantly, indicating the ideal cluster number.

inertia = []  # Inertia values for each k
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plotting the elbow curve to determine the optimal k
plt.figure(figsize=(8, 6))
plt.plot(k_range, inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.xticks(k_range)
plt.grid()
plt.show()

# Step 4: Apply K-Means clustering with the chosen number of clusters
# Based on the elbow method, assume we decide on 4 clusters for simplicity
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df = df.copy()
df['Cluster'] = kmeans.fit_predict(scaled_data)

print("Clustering complete! Cluster labels have been added to the DataFrame.")

# Step 5: Visualizing the clusters
# Plotting clusters for `SALES` vs. `QUANTITYORDERED`
plt.figure(figsize=(10, 8))
plt.scatter(df['SALES'], df['QUANTITYORDERED'], c=df['Cluster'], cmap='viridis', marker='o', alpha=0.5)
plt.title('K-Means Clustering Results')
plt.xlabel('Sales')
plt.ylabel('Quantity Ordered')
plt.colorbar(label='Cluster')
plt.grid()
plt.show()

df




