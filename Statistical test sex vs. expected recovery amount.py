"""Statistical test: sex vs. expected recovery amount
We were able to convince ourselves that there is no major jump in the average customer age just above and just below the $1000 threshold by doing a statistical test as well as exploring it graphically with a scatter plot.
We want to also test that the percentage of customers that are male does not jump as well across the $1000 threshold. We can start by exploring the range of $900 to $1100 and later adjust this range."""
from scipy import stats
import pandas as pd
df = pd.read_csv('bank_data.csv')

crosstab = pd.crosstab(df.loc[(df['expected_recovery_amount']<1100) & 
                              (df['expected_recovery_amount']>=900)]['recovery_strategy'], 
                       df['sex'])
print(crosstab)

chi2_stat, p_val, dof, ex = stats.chi2_contingency(crosstab)
print(p_val)