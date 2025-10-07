from google.oauth2 import service_account
from googleapiclient.discovery import build
from .config import GOOGLE_APPLICATION_CREDENTIALS, SCOPES

def get_service(api: str, version: str):
    """Авторизація + отримання даних для підключення до API"""
    creds = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS, scopes=SCOPES)

    return build(api, version, credentials=creds, cache_discovery=False)