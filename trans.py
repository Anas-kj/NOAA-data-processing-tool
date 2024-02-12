import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('./TABARKA 7 NOVEMBRE/combined.csv')

# Write the DataFrame to an Excel file
df.to_excel('combined.xlsx', index=False)

print("Conversion completed: combined.csv -> combined.xlsx")
