#!/usr/bin/env python

# Ohne Kohlensäure, bitte.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import sklearn.discriminant_analysis as lda
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics.ranking import roc_curve
from sklearn.metrics.ranking import roc_auc_score
import sys

data = pd.read_csv("wdbc.data", header=None)

# first column is patient ID, second is label
X = data.drop(columns=[0,1])
y = data[1]

model = lda.LinearDiscriminantAnalysis()
#model = sklearn.svm.SVC(kernel="linear")

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

cm = metrics.confusion_matrix(y_test, y_pred, labels=["M", "B"])
precision = metrics.precision_score(y_test, y_pred, pos_label="M")
recall = metrics.recall_score(y_test, y_pred, pos_label="M")
f1 = metrics.f1_score(y_test, y_pred, pos_label="M")

print(cm)
print("precision", precision)
print("recall", recall)
print("f1", f1)



y_scores = model.decision_function(X_test)


fpr, tpr, thresholds = roc_curve(y_test, y_scores, pos_label="M")
auc = roc_auc_score(y_test, y_scores)

fig, ax = plt.subplots(1, 1)
ax.set_title("ROC Curve for LDA on Wisconsin Breast Cancer Diagnostic Data")
ax.set_xlim(left = -0.01, right = 1.0)
ax.set_ylim(bottom = 0.0, top = 1.0)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")

# Baseline -- a random predictor
ax.plot([0, 1], [0, 1], color='navy', linestyle='--')

# Roc curve
ax.plot(fpr, tpr, marker=".", label=f"AUC = {auc}")
ax.legend(loc="lower right")

fig.savefig("breast-cancer-roc.png")
