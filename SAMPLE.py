import pandas as pd
import numpy as np
import re

df = pd.read_csv('sorted_employee_data.csv')

df = df.drop_duplicates()

def is_valid_email(email):
    if pd.isna(email):
        return False
    return re.match(r"[^@]+@[^@]+\.[^@]+", str(email)) is not None

df['email'] = df['email'].apply(lambda x: x if is_valid_email(x) else np.nan)

df['joining_date'] = pd.to_datetime(df['joining_date'], dayfirst=True)

median_date = df['joining_date'].dropna().median()
df['joining_date'].fillna(median_date, inplace=True)


df['salary'] = pd.to_numeric(df['salary'])
valid_salaries = df['salary'].dropna()
valid_salaries = valid_salaries[valid_salaries > 0]
median_salary = valid_salaries.median()
df['salary'] = df['salary'].apply(lambda x: median_salary if pd.isna(x) or x <= 0 else x)
df['email'] = df['email'].fillna('abc@gmail.com')
df['name'] = df['name'].fillna('Tejas')
df.to_csv('employee_cleaned2.csv', index=False)
print("Data cleaning completed. Cleaned data saved to 'employee_cleaned.csv'.")



                             


print(df)