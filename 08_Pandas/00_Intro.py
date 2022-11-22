import pandas as pd

d = {'name': ['A', 'B', 'C', 'D'], 'marks': [12, 15, 20, 32]}

df = pd.DataFrame(d)
print(df)

# converts dataframe into csv and saves it into a new file
df.to_csv('./files/dummy.csv')

df.to_html('./files/dummy.html')