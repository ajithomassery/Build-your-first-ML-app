# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sn6PQBnk7MQZassPYIrd1LdYGRhd1gg2
"""

import sklearn # import scikit learn

from sklearn import tree #import tree

features = [[140, 1], [130, 2], [120, 1], [170, 2],  [130, 2], [130, 1], [160, 2], ]

labels = [["apple"], ["orange"], ["apple"], ["orange"], ["orange"], ["apple"], ["orange"], ]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features,labels)

print(clf.predict([[130,2]]))