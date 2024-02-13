import pandas as pd
import os

directory = '/Users/anaskhouaja/pfe/TABARKA 7 NOVEMBRE'

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
combined_data.to_csv('/Users/anaskhouaja/pfe/TABARKA 7 NOVEMBRE/combined.csv', index=False)

#download files------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import os

def download_csv_files(base_url, start_year, end_year, base_download_path):
    if not os.path.exists(base_download_path):
        os.makedirs(base_download_path)

    for year in range(start_year, end_year + 1):
        year_url = f"{base_url}/{year}/"
        year_path = os.path.join(base_download_path, str(year))
        
        if not os.path.exists(year_path):
            os.makedirs(year_path)

        response = requests.get(year_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href and href.endswith('.csv'):
                    download_url = f"{year_url}{href}"
                    download_file(download_url, href, year_path)

def download_file(url, filename, year_path):
    response = requests.get(url)
    if response.status_code == 200:
        save_path = os.path.join(year_path, filename)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename} to {year_path}")

# Example usage
base_url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/'
start_year = 1929
end_year = 2024 # Update this based on the current year or your target year
base_download_path = '.'

download_csv_files(base_url, start_year, end_year, base_download_path)