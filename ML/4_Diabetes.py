import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("4_diabetes.csv")
df

print(df.info())

#Check for null or missing values
df.isnull().sum()

x = df.drop("Outcome" , axis = 1 )
y = df['Outcome']

sns.countplot(x=y)
y.value_counts()

# feature scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

# split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_scaled,y,test_size=0.25, random_state=0)
x_scaled

X_train.shape
X_test.shape

# model
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

error = []

for k in range(1,41):
    knn = KNeighborsClassifier(n_neighbors= k)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    error.append(np.mean(pred != y_test))

plt.figure(figsize=(12,10))
plt.xlabel("value of k")
plt.ylabel(" Error ")
plt.grid()
plt.xticks(range(1,41))
plt.plot(range(1,41), error, marker='.')

# least error for k value = 33 
knn = KNeighborsClassifier(n_neighbors= 33)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

#  Compute evaluation metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", conf_matrix)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Error Rate
error_rate = 1 - accuracy
print("\nError Rate:", error_rate)

# Precision
precision = precision_score(y_test, y_pred)
print("\nPrecision:", precision)

# Recall
recall = recall_score(y_test, y_pred)
print("\nRecall:", recall)

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
print(classification_report(y_test, y_pred))

