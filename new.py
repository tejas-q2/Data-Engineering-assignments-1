import pandas as pd
import numpy as np
import re

df = pd.read_csv('customers.csv')
df= df.drop_duplicates()


def is_valid_email(email):
    if pd.isna(email):
        return False
    return re.match(r"[^@]+@[^@]+\.[^@]+", str(email)) is not None

df['email'] = df['email'].apply(lambda x: x if is_valid_email(x) else np.nan)

valid_ages = df['age'].dropna()
valid_ages = valid_ages[valid_ages > 0]
median_age = valid_ages.median()
df['age'] = df['age'].apply(lambda x: median_age if pd.isna(x) or x <= 0 else x)
df['name'] = df['name'].fillna('Aditya')
df['city'] = df['city'].fillna('Pune')
df = df.dropna()
print(df)
