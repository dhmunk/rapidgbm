# Quickstart Guide

## Installation
```bash
pip install rapidgbm
```
---
## Classification Example
```python
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from rapidgbm import RapidGBMTuner

# Load and prepare data
X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Initialize and fit RapidGBMTuner
tuner = RapidGBMTuner(metric='auc', trials=4, verbosity=5, visualization=False)
tuner.fit(X_train, y_train)


AUC = roc_auc_score(y_test, tuner.predict_proba(X_test))
print("Area under the curve (AUC):", AUC)
```
##### Output
``` stdout
Area under the curve (AUC): 0.9987421383647799
```
---
## Regression Example
```python
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from rapidgbm import RapidGBMTuner

# Load and prepare data
X, y = fetch_california_housing(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Initialize and fit RapidGBMTuner
tuner = RapidGBMTuner(metric='mae', trials=4, verbosity=5, visualization=False)
tuner.fit(X_train, y_train)


mae = mean_squared_error(y_test, tuner.predict(X_test))
print("Mean squared error (MAE):", mae)
```
##### Output
``` stdout
Mean squared error (MAE): 0.18446140275456893
```