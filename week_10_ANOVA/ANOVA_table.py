import pandas as pd
import researchpy as rp

# From https://www.pythonfordatascience.org/anova-python/

df = pd.read_csv("../datasets/difficile.csv")
df.drop('person', axis= 1, inplace= True)

# Recoding value from numeric to string
df['dose'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace= True)

df.info()

rp.summary_cont(df['libido'])
rp.summary_cont(df['libido'].groupby(df['dose']))

