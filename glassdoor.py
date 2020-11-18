# -*- coding: utf-8 -*-
"""
Spyder Editor

Sayan Mondal.
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")
#df = pd.DataFrame(df)

#df.info()

cols = df.columns

df['staff_payment_type'] = df['Salary Estimate'].apply(lambda x: 'Hourly wage' if x=='-1' else 'Regular salary')

#df['salary_range'] = df['Salary Estimate'].apply(lambda x: 1 if x.lower() else x)

df['salary_range'] = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
df['salary_range'] = df['salary_range'].apply(lambda x: x.replace('K','').replace('$',''))
df['salary_minimum'] = df['salary_range'].apply(lambda x: x.split('-')[0])
df['salary_maximum'] = df['salary_range'].apply(lambda x: x.split('-')[1])

#df['salary_minimum'] = pd.to_numeric(df['salary_minimum'])
#df['salary_maximum'] = pd.to_numeric(df['salary_maximum'])  

  

