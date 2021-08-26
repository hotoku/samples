"""
これは、デッドロックになる
"""


from concurrent.futures import ProcessPoolExecutor

import lightgbm as lgb
from sklearn.datasets import make_classification

X_train, y_tarin = make_classification(
    n_samples=100,
    n_features=20
)

lgb_model = lgb.LGBMRegressor(random_state=0)
lgb_predictor = lgb_model.fit(X_train, y_tarin)


def doit():
    X_pred, y_pred = make_classification(
        n_samples=20,
        n_features=20
    )
    y_hat = lgb_predictor.predict(X_pred)
    return y_hat, y_pred


with ProcessPoolExecutor() as ex:
    fs = []
    for i in range(10):
        print(f"submit {i}")
        future = ex.submit(doit)
        fs.append(future)

print(fs)
