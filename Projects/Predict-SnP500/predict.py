# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:05:10 2016

@author: donaldfung
"""
import assemble
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.feature_selection import SelectKBest, f_classif
import settings
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

class Model():
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        
    def predict(self):
        lr = LinearRegression()
        lr.fit(self.X_train, self.y_train)
        y_train_pred = lr.predict(self.X_train)
        y_test_pred = lr.predict(self.X_test)
        train_error = mean_absolute_error(self.y_train, y_train_pred)
        test_error = mean_absolute_error(self.y_test, y_test_pred)
        print("mae on training data:", train_error)
        print("mae on test data:", test_error)
        print("r squared on training data:",r2_score(self.y_train, y_train_pred))   
        print("r squared on testing data:", r2_score(self.y_test, y_test_pred))
        #self.feature_selection(self.X_train, self.y_train)
        
    def feature_selection(self, X, y):
        size_k = len(settings.features)
        selector = SelectKBest(f_classif, k=size_k)
        selector.fit(X, y)        
        scores = -np.log10(selector.scores_)
        plt.bar(range(len(settings.features)), scores)
        plt.xticks(range(len(settings.features)), settings.features, rotation='vertical')
        plt.show()
        
def run():
    data = assemble.Data()
    data.read()
    
if __name__ == "__main__":
     run()