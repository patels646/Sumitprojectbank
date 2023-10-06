"""Regression modeling: adjusting the window
The regression coefficient for the true threshold was statistically significant with an estimated impact of around $278 and a 95 percent confidence interval of $132 to $424. This is much larger than the incremental cost of running the higher recovery strategy which was $50 per customer. At this point, we are feeling reasonably confident that the higher recovery strategy is worth the additional costs of the program for customers just above and just below the threshold.
Before showing this to our managers, we want to convince ourselves that this result wasn't due just to us choosing a window of $900 to $1100 for the expected recovery amount. If the higher recovery strategy really had an impact of an extra few hundred dollars, then we should see a similar regression coefficient if we choose a slightly bigger or a slightly smaller window for the expected recovery amount. Let's repeat this analysis for the window of expected recovery amount from $950 to $1050 to see if we get similar results."""
# Redefine era_950_1050 with the indicator variable included
import pandas as pd
import numpy as np
df = pd.read_csv('bank_data.csv')
era_950_1050 = df.loc[(df['expected_recovery_amount'] < 1050) & 
                      (df['expected_recovery_amount'] >= 950)]
era_950_1050['indicator_1000'] = (era_950_1050['expected_recovery_amount'] >= 1000).astype(int)

# Define X and y
X = era_950_1050[['expected_recovery_amount','indicator_1000']]
y = era_950_1050['actual_recovery_amount']

# Add a constant term to the independent variable (X)
X = sm.add_constant(X)

# Build a linear regression model
model = sm.OLS(y, X).fit()

# Print the model summary
print(model.summary())