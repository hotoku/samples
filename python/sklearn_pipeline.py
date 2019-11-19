#!/usr/bin/env python


import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline


X_train = pd.DataFrame(dict(
    a=np.arange(10)
))
Y_train = np.arange(10)



class SampleImputer(BaseEstimator, TransformerMixin):
    def __init__(self, num):
        self.num = num

    def fit(self, x, y):
        return self

    def transform(self, df):
        df.loc[:,"NUM"] = self.num
        return df

class SimpleEstimator(BaseEstimator, RegressorMixin):
    def __init__(self):
        pass

    def fit(self, x, y):
        return self

    def predict(self, x):
        # import pdb; pdb.set_trace()
        print(f"est predict: {x['NUM']}")
        return x["NUM"]

pl = Pipeline([
    ("imp", SampleImputer(1)),
    ("est", SimpleEstimator())
])

params = dict(
    imp__num=[0, 10, 20]
)

# cross_val_score(pl, X_train, Y_train, cv=5, scoring="max_error")
gcv = GridSearchCV(pl, params, cv=5, scoring="max_error")
gcv.fit(X_train, Y_train)
