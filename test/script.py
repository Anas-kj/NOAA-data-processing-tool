import pandas as pd
import os

def combine_csv_files(directory):
    csv_files = sorted([file for file in os.listdir(directory) if file.endswith('.csv')])

    # Initialize an empty list to store DataFrames
    data_frames = []

    # Loop through each CSV file, read its data into a DataFrame, and store it in the list
    for file in csv_files:
        print(f'Loading file {file}...')
        file_path = os.path.join(directory, file)
        data = pd.read_csv(file_path)  # Read CSV file
        data_frames.append(data)  # Append DataFrame to list

    combined_data = pd.concat(data_frames, ignore_index=True)
    
    # Save combined data as an Excel file
    combined_excel_path = os.path.join(directory, 'combined.xlsx')
    combined_data.to_excel(combined_excel_path, index=False)
    print(f"Combined data saved as '{combined_excel_path}'.")
    
    for file in csv_files:
        os.remove(os.path.join(directory, file))
    print("Individual CSV files deleted.")

# List of directories containing CSV files
directories = [
    '/Users/Anas/pfe_test/EL_BORMA',
    '/Users/Anas/pfe_test/GABES',
    '/Users/Anas/pfe_test/GAFSA',
    '/Users/Anas/pfe_test/HABIB_BOURGUIBA_INTL',
    '/Users/Anas/pfe_test/JANDOUBA',
    '/Users/Anas/pfe_test/KAIROUAN',
    '/Users/Anas/pfe_test/KEBILI',
    '/Users/Anas/pfe_test/KELIBIA',
    '/Users/Anas/pfe_test/LE_KEF',
    '/Users/Anas/pfe_test/MEDENINE',
    '/Users/Anas/pfe_test/MONASTIR-SKANES',
    '/Users/Anas/pfe_test/NABEUL',
    '/Users/Anas/pfe_test/NEFTA',
    '/Users/Anas/pfe_test/REMADA',
    '/Users/Anas/pfe_test/SIDI_AHMED_AIR_BASE',
    '/Users/Anas/pfe_test/SIDI_BOUZID',
    '/Users/Anas/pfe_test/SILIANA',
    '/Users/Anas/pfe_test/TABARKA_7_NOVEMBRE',
    '/Users/Anas/pfe_test/TATAOUINE',
    '/Users/Anas/pfe_test/THALA',
    '/Users/Anas/pfe_test/THYNA',
    '/Users/Anas/pfe_test/ZARZIS'
]

# Combine CSV files in each directory
for directory in directories:
    print(f"Processing directory: {directory}")
    combine_csv_files(directory)
