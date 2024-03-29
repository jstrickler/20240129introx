import pandas as pd

df = pd.read_csv('../DATA/sales_records.csv')  # Read CSV data into dataframe. Pandas automatically uses the first row as column names

print(df.describe())  # Get statistics on the numeric columns (use `df.describe(include='O')` for text columns)
print()

print(df.info())  # Get information on all the columns ('object' means text/string)
print()

print(df.head(5))  # Display first 5 rows of the dataframe (`df.describe(__n__)` displays n rows)

df['total_sales'] = df['Units Sold'] * df['Unit Price']
print(df)

print(df.head(5))

df.insert(0, 'sales', df['total_sales'])
df.drop('total_sales', axis=1, inplace=True)
print(df.head(5))

