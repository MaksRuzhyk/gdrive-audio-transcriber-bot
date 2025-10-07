import io

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
        while next_page_token:                                                     #відредактувати функцію, прибрати дублі. НЕ ЗАБУТИ!!!
            next_page = self.drive.files().list(q=q, pageSize=10, fields=field,
                                                pageToken=next_page_token).execute()
            next_page_token = next_page.get('nextPageToken')
            calls.extend(next_page.get("files", []))

        return calls

    def download_file(self, file_id: str, filename: str):
        """логіка самого завантаження дзвінків"""
        self.dest_dir.mkdir(parents=True, exist_ok=True)
        path = self.dest_dir / filename
        if path.exists():
            return path

        request = self.drive.files().get_media(fileId=file_id)

        with io.FileIO(path, 'wb') as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))

        return path

    def download_all_calls(self):
        """Функція для завантаження всіх файлі які знайшли в директорії"""
        files = self.get_list_calls()

        result = []
        for file in files:
            name = file['name']
            path = self.dest_dir / name
            if path.exists():
                result.append(path)
                continue
            try:
                saved = self.download_file(file['id'], name)
                result.append(saved)
            except Exception as e:
                print(f'Skip {name}: {e}')
        return result

    """Подумати над варіантом без завантаження дзвінків локально"""