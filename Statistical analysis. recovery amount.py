"""Statistical analysis: recovery amount
Just as we did with age, we can perform statistical tests to see if the actual recovery amount has a discontinuity above the $1000 threshold. We are going to do this for two different windows of the expected recovery amount $900 to $1100 and for a narrow range of $950 to $1050 to see if our results are consistent.
Again, the statistical test we will use is the Kruskal-Wallis test, a test that makes no assumptions about the distribution of the actual recovery amount."""
# Compute average actual recovery amount just below and above the threshold
from scipy import stats
import pandas as pd

df = pd.read_csv('bank_data.csv')

# Group the DataFrame by 'recovery_strategy'
by_recovery_strategy = df.groupby(['recovery_strategy'])

# Describe 'actual_recovery_amount' for each group
description = by_recovery_strategy['actual_recovery_amount'].describe().unstack()
print(description)

# Perform Kruskal-Wallis test for the entire range
era_900_1100 = df.loc[(df['expected_recovery_amount'] < 1100) & (df['expected_recovery_amount'] >= 900)]
Level_0_actual = era_900_1100.loc[df['recovery_strategy'] == 'Level 0 Recovery']['actual_recovery_amount']
Level_1_actual = era_900_1100.loc[df['recovery_strategy'] == 'Level 1 Recovery']['actual_recovery_amount']
kruskal_result = stats.kruskal(Level_0_actual, Level_1_actual)
print("Kruskal-Wallis Test (900-1100):", kruskal_result)

# Repeat for a smaller range of $950 to $1050
era_950_1050 = df.loc[(df['expected_recovery_amount'] < 1050) & (df['expected_recovery_amount'] >= 950)]
Level_0_actual = era_950_1050.loc[df['recovery_strategy'] == 'Level 0 Recovery']['actual_recovery_amount']
Level_1_actual = era_950_1050.loc[df['recovery_strategy'] == 'Level 1 Recovery']['actual_recovery_amount']
kruskal_result = stats.kruskal(Level_0_actual, Level_1_actual)
print("Kruskal-Wallis Test (950-1050):", kruskal_result)