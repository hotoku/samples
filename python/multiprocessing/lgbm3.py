"""
別のプロセスで作られたモデルならロードできる
"""


import pickle
import sys
import os
from concurrent.futures import ProcessPoolExecutor

import lightgbm as lgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import joblib

joblib_file = "lgbm3.joblib"
pickle_file = "lgbm3.pickle"


if not os.path.exists(joblib_file):
    X, y = make_classification(
        n_samples=100,
        n_features=20
    )

    splitted = train_test_split(X, y)
    X_train, X_test = splitted[:2]
    y_train, y_test = splitted[2:]

    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)
    yhat = model.predict(X_test)
    print(yhat)

    joblib.dump(model, joblib_file)
    with open(pickle_file, "wb") as f:
        import pickle
        pickle.dump([X_train, X_test, y_train, y_test],
                    f)
    sys.exit(0)


def doit():
    model = joblib.load(joblib_file)
    with open(pickle_file, "rb") as f:
        data = pickle.load(f)
    y_hat = model.predict(data[1])
    return y_hat


with ProcessPoolExecutor() as ex:
    fs = []
    for i in range(10):
        print(f"submit {i}")
        future = ex.submit(doit)
        fs.append(future)

for f in fs:
    print(f.result())
