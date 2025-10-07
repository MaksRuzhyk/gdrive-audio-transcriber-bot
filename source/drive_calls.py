import io
from dataclasses import fields
from pathlib import Path

from googleapiclient.http import MediaIoBaseDownload

from .auth_service_account import get_service
from .config import DRIVE_FOLDER_ID, DOWNLOAD_DIR

class DriveCalls:
    """Клас для отримання списку дзвінків і їх завантаження в локальну директорію"""
    def __init__(self, folder_id=DRIVE_FOLDER_ID, dest_dir=DOWNLOAD_DIR):
        self.folder_id = folder_id
        self.dest_dir = dest_dir
        self.drive = get_service('drive', 'v3')

    def get_list_calls(self):
        """Отримуємо список дзвінків з директорії, фільтруємо по формату audio/mpeg"""
        calls = []

        q = f"'{self.folder_id}' in parents and mimeType='audio/mpeg' and trashed=false"
        field = 'nextPageToken, files(id, name, mimeType)'

        result = self.drive.files().list(q=q, pageSize=10, fields=field).execute()
        calls.extend(result.get('files', []))
        next_page_token = result.get('nextPageToken')
        while next_page_token:                                                     #відредактувати функцію, приблрати дублі. НЕ ЗАБУТИ!!!
            next_page = self.drive.files().list(q=q, pageSize=10, fields=field,
                                                pageToken=next_page_token).execute()
            next_page_token = next_page.get('nextPageToken')
            calls.extend(next_page.get("files", []))

        return f'Results -> {calls}, {len(calls)}'


