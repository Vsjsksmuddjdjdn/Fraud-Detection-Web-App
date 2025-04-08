# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1otMxOg_BcWhzAIOb5xYs3isfRK6s3lx3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

from google.colab import files
uploaded = files.upload()

data = pd.read_csv("creditcard.csv")

data.head()

print(data.shape)
print(data.describe())

Fraud = data[data['Class']==1]
valid = data[data['Class']==0]
outlierFraction = len(Fraud)/float(len(valid))
print(outlierFraction)
print('Fraud Cases: {}'.format(len(data[data['Class']==1])))
print('Valid Transaction: {}'.format(len(data[data['Class']==0])))

print("Amount details of Fraudulent Transaction")
Fraud.Amount.describe()

print("Amount details of Valid Transaction")
valid.Amount.describe()

corrmat = data.corr()
fig = plt.figure(figsize=(6,6))
sns.heatmap(corrmat,vmax=.8,square=True)
plt.show()

X = data.drop(['Class'],axis=1)
Y = data["Class"]
print(X.shape)
print(Y.shape)
xData=X.values
yData=Y.values

from sklearn.model_selection import train_test_split
xTrain,xTest,yTrain,yTest = train_test_split(xData,yData,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(class_weight='balanced')
rfc.fit(xTrain, yTrain)
yPred = rfc.predict(xTest)

from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score, matthews_corrcoef
from sklearn.metrics import confusion_matrix

n_outlier = len(Fraud)
n_error = (yPred != yTest).sum()

print("The Model Uses Random Forest Classifier")

acc = accuracy_score(yTest, yPred)
print("The Accuracy of Model is {}".format(acc))

prec = precision_score(yTest, yPred)
print("The Accuracy of Model is {}".format(prec))

rec = recall_score(yTest, yPred)
print("The Accuracy of Model is {}".format(rec))

f1 = f1_score(yTest, yPred)
print("The Accuracy of Model is {}".format(f1))

MCC = matthews_corrcoef(yTest, yPred)
print("The Matthews correlation coefficient is{}".format(MCC))

LABELS = ['Normal','Fraud']
conf_matrix = confusion_matrix(yTest,yPred)
plt.figure(figsize=(6,6))
sns.heatmap(confusion_matrix(yTest,yPred),xticklabels=LABELS,yticklabels=LABELS,annot=True,fmt="d");
plt.title("Confusion Matrix")
plt.ylabel('True Class')
plt.xlabel('Predicted Class')
plt.show()

!pip install streamlit

import joblib
joblib.dump(rfc, "fraud_model_u.pkl")

from google.colab import files
files.download('fraud_model_u.pkl')

