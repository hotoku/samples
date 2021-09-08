"""
これは、デッドロックになる
"""


from concurrent.futures import ProcessPoolExecutor

import lightgbm as lgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import joblib

X, y = make_classification(
    n_samples=100,
    n_features=20,
    random_state=0
)

splitted = train_test_split(X, y)
X_train, X_test = splitted[:2]
y_train, y_test = splitted[2:]


lgb_model = lgb.LGBMRegressor(random_state=0)
lgb_model.fit(X_train, y_train)

dumpto = "lgbm2.joblib"
joblib.dump(lgb_model, dumpto)


y_hat = lgb_model.predict(X_test)
print(y_hat)


def doit():
    model = joblib.load(dumpto)
    y_hat = model.predict(X_test)
    return y_hat


with ProcessPoolExecutor() as ex:
    fs = []
    for i in range(10):
        print(f"submit {i}")
        future = ex.submit(doit)
        fs.append(future)


for f in fs:
    print(f)
