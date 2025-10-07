import os
from dotenv import load_dotenv
from pathlib import Path

"""Завантажуємо змінні з .env, створюємо додаткові теки"""

load_dotenv()

#Підвантаження ID директорії з дзвінками і ID звіту

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

SHEET_ID = os.getenv("SHEET_ID")

if not all([GOOGLE_APPLICATION_CREDENTIALS, DRIVE_FOLDER_ID, SHEET_ID]):
    raise ValueError('GOOGLE_APPLICATION_CREDENTIALS or FOLDER_ID or SHEET_ID not found in .env file.')

#Дозволи для роботи з API

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
]

#Перевіряємо чи існує локальна директорія з дзвінками якщо ні створюємо в корені проєкту

BASE_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = BASE_DIR / os.getenv("DOWNLOAD_DIR", 'data/audio')
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

#Статус, не впевнений, що він тут треба
print('-' * 100)
print(f'GOOGLE_APPLICATION_CREDENTIALS -> OK \n')
print(f'DRIVE_FOLDER_ID -> OK\n')
print(f'SHEET_ID -> OK\n')
print(f'DOWNLOAD_DIR - {DOWNLOAD_DIR.resolve()}')
print('-' * 100)