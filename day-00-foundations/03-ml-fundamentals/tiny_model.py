"""Minimal supervised example. Requires: pip install scikit-learn numpy"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

rng = np.random.default_rng(42)
distance = rng.uniform(1, 30, size=200).reshape(-1, 1)
time_min = 8 + 2.5 * distance.ravel() + rng.normal(0, 4, size=200)

X_tr, X_te, y_tr, y_te = train_test_split(distance, time_min, test_size=0.2)
model = LinearRegression().fit(X_tr, y_tr)
print(f"Test MAE: {mean_absolute_error(y_te, model.predict(X_te)):.2f} min")
print(f"Predicted time for 15 km: {model.predict([[15]])[0]:.1f} min")
