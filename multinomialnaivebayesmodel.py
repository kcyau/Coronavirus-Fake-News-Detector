# -*- coding: utf-8 -*-
"""MultinomialNaiveBayesModel

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c3lFKhG0bWicsgtYSyhhEnhSmF1IuMSY
"""

import pandas as pd
import numpy as np
import itertools
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import max_error

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline

df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('coronaNews.csv')

df1 = df1.dropna()
df2 = df2.dropna()

y1 = df1.label
y2 = df2.label

df1 = df1.drop('label', axis = 1)
df2 = df2.drop('label', axis = 1)

X_train, trash_test, y_train, trash_train = train_test_split(df1['text'], y1, train_size=0.9, random_state=53)
X_test, throw_test, y_test, throw_train = train_test_split(df2['text'], y2, train_size=0.9, random_state=53)

count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train.values.astype('U'))
count_test = count_vectorizer.transform(X_test.values.astype('U'))

tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.9)
tfidf_train = tfidf_vectorizer.fit_transform(X_train.values.astype('U'))
tfidf_test = tfidf_vectorizer.transform(X_test.values.astype('U'))

mn_count_clf = MultinomialNB(alpha=0.1)

mn_count_clf.fit(count_train, y_train)
pred = mn_count_clf.predict(count_test)
score = metrics.accuracy_score(y_test, pred)
#print("accuracy:   %0.3f" % score)
#print(f1_score(y_test, pred, average="macro"))
print(classification_report(y_test, pred))

