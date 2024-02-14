import requests
import os
import shutil

def create_station_directories(base_download_path, stations):
    for station in stations:
        station_path = os.path.join(base_download_path, station['station'])
        if not os.path.exists(station_path):
            os.makedirs(station_path)

def move_csv_files(base_url, start_year, end_year, base_download_path, stations):
    for year in range(start_year, end_year + 1):
        year_path = os.path.join(base_download_path, str(year))

        for station in stations:
            station_path = os.path.join(year_path, station['station'])

            if not os.path.exists(station_path):
                continue

            usaf_prefix = str(station['USAF'])
            files = [f for f in os.listdir(year_path) if f.startswith(usaf_prefix) and f.endswith('.csv')]
            for file in files:
                src = os.path.join(year_path, file)
                dst = os.path.join(station_path, file)
                shutil.move(src, dst)
                print(f"Moved {file} to {station_path}")

# Example usage
base_url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access'
start_year = 1929
end_year = 2024  # Update this based on the current year or your target year
base_download_path = '.'

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

create_station_directories(base_download_path, stations)
move_csv_files(base_url, start_year, end_year, base_download_path, stations)
