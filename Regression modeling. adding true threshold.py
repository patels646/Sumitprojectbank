"""Regression modeling: adding true threshold
From the first model, we see that the regression coefficient is statistically significant for the expected recovery amount and the adjusted R-squared value was about 0.26. As we saw from the graph, on average the actual recovery amount increases as the expected recovery amount increases. We could add polynomial terms of expected recovery amount (such as the squared value of expected recovery amount) to the model but, for the purposes of this practice, let's stick with using just the linear term.
The second model adds an indicator of the true threshold to the model. If there was no impact of the higher recovery strategy on the actual recovery amount, then we would expect that the relationship between the expected recovery amount and the actual recovery amount would be continuous."""
import pandas as pd
import statsmodels.api as sm  # Import statsmodels.api

df = pd.read_csv('bank_data.csv')

df['indicator_1000'] = (df['expected_recovery_amount'] >= 1000).astype(int)

# Filter data for expected recovery amount between $900 and $1100
era_900_1100 = df[(df['expected_recovery_amount'] >= 900) & (df['expected_recovery_amount'] < 1100)]

# Define X and y
X = era_900_1100[['expected_recovery_amount', 'indicator_1000']]
y = era_900_1100['actual_recovery_amount']

# Add a constant term to the independent variable (X)
X = sm.add_constant(X)

# Build a linear regression model
model = sm.OLS(y, X).fit()

# Print the model summary
print(model.summary())
