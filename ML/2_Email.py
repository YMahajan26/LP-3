import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("2_emails.csv")

df.head()
df.shape
print(df.info())

# step 2: data preprocessing
# check for missing values
print("Missing Values: ", df.isnull().sum().sum()) # expecting 0 for clean data

# step 3: Separate the feature X (email text) and the target y (spam label).
X = df.drop(["Email No.", "Prediction"], axis=1) #ip
y = df["Prediction"]  #op

set(X.dtypes)
sns.countplot(x=y)
y.value_counts()

# Feature scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_scaled

# # 3. Split the dataset into training and testing sets (75% training, 25% testing)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=0)

X_train.shape
X_test.shape

#  K-Nearest Neighbors (KNN) Model

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Evalution 

from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report

ConfusionMatrixDisplay.from_predictions(y_test, y_pred_knn)

y_test.value_counts()

# Evaluate KNN
print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))
print("KNN Classification Report:\n", classification_report(y_test, y_pred_knn))
print("KNN Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))

# SVM

from sklearn.svm import SVC

svm = SVC(kernel='linear')
svm.fit(X_train,y_train)
y_pred_svm = svm.predict(X_test)  # Predict on test data

ConfusionMatrixDisplay.from_predictions(y_test, y_pred_svm)

# Evaluate SVM
print("\nSVM Accuracy:", accuracy_score(y_test, y_pred_svm))
print("SVM Classification Report:\n", classification_report(y_test, y_pred_svm))
print("SVM Confusion Matrix:\n", confusion_matrix(y_test, y_pred_svm))

# =========================extra========================

# knn improvement 
import numpy as np

error = []
for k in range(1,41):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    error.append(np.mean(pred != y_test))

error

# knn with n=1 as it has least error
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Evaluate KNN
print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))
print("KNN Classification Report:\n", classification_report(y_test, y_pred_knn))
print("KNN Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))

# SVM other kernel

svm = SVC(kernel='rbf') 
svm.fit(X_train, y_train)  
y_pred_svm = svm.predict(X_test) 

print("\nSVM(RBF) Accuracy:", accuracy_score(y_test, y_pred_svm))
print("SVM Classification Report:\n", classification_report(y_test, y_pred_svm))
print("SVM Confusion Matrix:\n", confusion_matrix(y_test, y_pred_svm))

# 2. kernel = poly

svm = SVC(kernel='poly') 
svm.fit(X_train, y_train)  
y_pred_svm = svm.predict(X_test) 

print("\nSVM(poly) Accuracy:", accuracy_score(y_test, y_pred_svm))
print("SVM Classification Report:\n", classification_report(y_test, y_pred_svm))
print("SVM Confusion Matrix:\n", confusion_matrix(y_test, y_pred_svm))

# SVM
# linear = 97%  ===best
# rbf = 94 %
# poly = 75 %


