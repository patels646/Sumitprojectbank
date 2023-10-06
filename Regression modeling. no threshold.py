"""Regression modeling: no threshold
We now want to take a regression-based approach to estimate the impact of the program at the $1000 threshold using the data that is just above and just below the threshold. In order to do that, we will build two models. The first model does not have a threshold while the second model will include a threshold.
The first model predicts the actual recovery amount (outcome or dependent variable) as a function of the expected recovery amount (input or independent variable). We expect that there will be a strong positive relationship between these two variables."""
import statsmodels.api as sm
import pandas as pd
import numpy as np
df = pd.read_csv('bank_data.csv')

era_900_1100 = df.loc[(df['expected_recovery_amount'] < 1100) & (df['expected_recovery_amount'] >= 900)]

X = era_900_1100['expected_recovery_amount']
y = era_900_1100['actual_recovery_amount']

# Add a constant term to the independent variable (X)
X = sm.add_constant(X)

# Build a linear regression model
model = sm.OLS(y, X).fit()

# Get predictions from the model
predictions = model.predict(X)

# Print the model summary statistics
print(model.summary())