import pandas as pd

# create data
dat = {'x': [10, 11, 12, 10, 11],
       'y': [20, 21, 22, 20, 21],
       'z': [30, 31, 32, 30, 31]}

df = pd.DataFrame(dat)
print(df)

# duplicate rows
df.duplicated()

# drop duplicate rows
df.drop_duplicates(inplace=True)