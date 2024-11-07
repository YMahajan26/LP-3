import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("3_churn_Modelling.csv")

df.shape
print(df.info())

# separate features and target value 
x = df[["CreditScore",	"Age",	"Tenure",	"Balance",	"NumOfProducts"	,"HasCrCard","IsActiveMember","EstimatedSalary"	]]
y = df["Exited"]

sns.countplot(x=y)

y.value_counts()

# Normalize
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_scaled

# split data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_scaled, y, random_state=0, test_size=0.25)

X_train.shape
X_test.shape

#  ANN from sklearn 
from sklearn.neural_network import MLPClassifier

ann = MLPClassifier(hidden_layer_sizes=(100,100,100),
                   random_state=0,
                   max_iter=100,
                   activation='relu')

ann.fit(X_train, y_train)
y_pred = ann.predict(X_test)
y_pred

y_test.value_counts()

from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report,confusion_matrix

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

print(classification_report(y_test, y_pred))


# Balance the imbalanced class
# !pip install imbalanced-learn

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=0)
x_res, y_res = ros.fit_resample(x,y)
x_res.shape

# Normalize
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_res)
x_scaled

# split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_scaled, y_res, random_state=0, test_size=0.25)
X_train.shape
X_test.shape

#  ANN from sklearn 
from sklearn.neural_network import MLPClassifier
ann = MLPClassifier(hidden_layer_sizes=(100,100,100),
                   random_state=0,
                   max_iter=100,
                   activation='relu')

ann.fit(X_train, y_train)
y_pred = ann.predict(X_test)
y_test.value_counts()

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

print(classification_report(y_test, y_pred))

