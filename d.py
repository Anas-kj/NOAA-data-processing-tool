import requests
from bs4 import BeautifulSoup
import os

# Define the array of stations
stations = [
    {'USAF': 607100, 'station': 'TABARKA 7 NOVEMBRE'},
    {'USAF': 607140, 'station': 'SIDI AHMED AIR BASE'},
    {'USAF': 607150, 'station': 'CARTHAGE'},
    {'USAF': 607200, 'station': 'KELIBIA'},
    {'USAF': 607230, 'station': 'BEJA'},
    {'USAF': 607250, 'station': 'JANDOUBA'},
    {'USAF': 607280, 'station': 'NABEUL'},
    {'USAF': 607320, 'station': 'LE KEF'},
    {'USAF': 607340, 'station': 'SILIANA'},
    {'USAF': 607350, 'station': 'KAIROUAN'},
    {'USAF': 607380, 'station': 'THALA'},
    {'USAF': 607400, 'station': 'MONASTIR-SKANES'},
    {'USAF': 607403, 'station': 'HABIB BOURGUIBA INTL'},
    {'USAF': 607450, 'station': 'GAFSA'},
    {'USAF': 607480, 'station': 'SIDI BOUZID'},
    {'USAF': 607500, 'station': 'THYNA'},
    {'USAF': 607600, 'station': 'NEFTA'},
    {'USAF': 607640, 'station': 'KEBILI'},
    {'USAF': 607650, 'station': 'GABES'},
    {'USAF': 607690, 'station': 'ZARZIS'},
    {'USAF': 607700, 'station': 'MEDENINE'},
    {'USAF': 607720, 'station': 'TATAOUINE'},
    {'USAF': 607750, 'station': 'REMADA'},
    {'USAF': 607800, 'station': 'EL BORMA'}
]

def download_csv(dir,usaf,url):
    for year in range(1994,2025):
        response= requests.get(url)
        if response.status_code ==200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                if link['href'].startswith(usaf) and link['href'].endswith(".csv"):
                    csv_url = url +f"{year}/"
                    csv_response = requests.get(csv_url)
                    if csv_response.status_code == 200:
                        with open(f"{dir}/{usaf}-{year}.csv", 'wb') as f:
                            f.write(csv_response.content)
                            print(f"Downloaded: {usaf}-{year}.csv")
                    else:
                        print(f"Failed to download CSV for {station['station']} in {year}")
        else:
            print(f"Failed to access {url}")


def download_station_csv(station,url):
    station_name = station['station'].replace(" ","_")
    directory = f"./{station_name}"
    os.makedirs(directory, exist_ok=True)
    download_csv(directory,station['USAF'],url)





#PP
url = "https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/"
for station in stations:
    download_station_csv(station,url)