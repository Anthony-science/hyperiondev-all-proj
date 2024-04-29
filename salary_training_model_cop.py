import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset (assuming the file "Salary_dataset.csv" is available)
data = pd.read_csv("Salary_dataset.csv")

# Extract features (X) and target (y)
X = data.iloc[:, 1].values.reshape(-1, 1)
y = data.iloc[:, 2].values

# Split the data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = model.predict(X_test)

# Calculate mean squared error
mse = mean_squared_error(Y_test, Y_pred)

# Print relevant information
print("Dataset summary:")
print(data.head())
print("\nTrain-test split summary:")
print(f"Number of training samples: {len(X_train)}")
print(f"Number of test samples: {len(X_test)}")
print("\nModel summary:")
print(f"Coefficient (slope): {model.coef_[0]}")
print(f"Intercept (bias): {model.intercept_}")
print("\nMean squared error:", mse)

# Visualize the regression line
plt.scatter(X_test, Y_test, color='blue', label='Actual')
plt.plot(X_test, Y_pred, color='red', label='Predicted')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Linear Regression: Salary vs. Experience')
plt.legend()
plt.show()
