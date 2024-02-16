import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('./BEJA/combined.xlsx')

# Convert 'DATE' column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Extract year, month, and day into separate columns
df['YEAR'] = df['DATE'].dt.year
df['MONTH'] = df['DATE'].dt.month
df['DAY'] = df['DATE'].dt.day

# Drop the original 'DATE' column
df = df.drop(columns=['DATE'])

# Reorder columns to place 'YEAR' in position 2, 'MONTH' in position 3, and 'DAY' in position 4
cols = list(df.columns)
cols.insert(1, 'YEAR')
cols.insert(2, 'MONTH')
cols.insert(3, 'DAY')
df = df.reindex(columns=cols)

# Print the head of the DataFrame to verify the changes
print(df.head())

# Save the modified DataFrame to a new Excel file
df.to_excel('modified.xlsx', index=False)
