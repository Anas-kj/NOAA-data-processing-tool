import pandas as pd
import glob

# List all CSV files in the directory
csv_files = glob.glob('*.csv')

# Create a Pandas Excel writer using xlsxwriter as the engine
with pd.ExcelWriter('combined_data.xlsx', engine='xlsxwriter') as writer:
    for csv_file in csv_files:
        # Read CSV into Pandas DataFrame
        df = pd.read_csv(csv_file)
        # Extract file name without extension for sheet name
        sheet_name = csv_file.split('.')[0]
        # Write DataFrame to Excel as a sheet with table formatting
        df.to_excel(writer, sheet_name=sheet_name, index=False, engine='xlsxwriter')

        # Get the xlsxwriter workbook and worksheet objects
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Add table formatting
        max_row = len(df)
        max_col = len(df.columns)
        worksheet.add_table(0, 0, max_row, max_col - 1, {'header_row': True})

print("Combined data saved to combined_data.xlsx")
