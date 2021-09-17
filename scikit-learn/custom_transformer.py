import numpy as np
from sklearn.datasets import load_boston
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

data = load_boston()

y = data["target"]
X = data["data"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Custom transformation step 

def sqrt_features(data):
    data = np.sqrt(data)
    return data

# Scikit-learn compatible transformer
sqrt_transformer = FunctionTransformer(sqrt_features)

steps = [('scaler', sqrt_transformer),
         ('regressor', DecisionTreeRegressor())]
pipeline = Pipeline(steps)

# Fit the model
regressor = pipeline.fit(X_train, y_train)
regressor.predict(X_test)
