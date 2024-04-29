from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt

from joblib import dump

data = pd.read_csv("Salary_dataset.csv")

X = data.iloc[:, 0].values.reshape(-1, 1)
y = data.iloc[:, 1].values

print(data.head())

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

mse = mean_squared_error(Y_test, Y_pred)
print("Mean squared error", mse)
