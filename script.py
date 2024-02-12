import pandas as pd
import os

# Directory containing your CSV files
directory = '/Users/anaskhouaja/pfe/TABARKA 7 NOVEMBRE'

# Get list of CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through each CSV file, read its data into a DataFrame, and store it in the list
for file in csv_files:
    file_path = os.path.join(directory, file)
    data = pd.read_csv(file_path)  # Read CSV file
    data_frames.append(data)  # Append DataFrame to list

# Concatenate all DataFrames in the list
combined_data = pd.concat(data_frames, ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv('/Users/anaskhouaja/pfe/TABARKA 7 NOVEMBRE/combined.csv', index=False)
