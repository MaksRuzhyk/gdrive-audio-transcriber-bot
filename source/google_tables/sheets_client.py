from source.auth_service_account import get_service
from source.config import SHEET_ID

class SheetsClient:
    def __init__(self, sheet_id: str = SHEET_ID, sheets_title: str = "Page1"):
        self.sheet_id = sheet_id
        self.sheets_title = sheets_title
        self.sheets_api = get_service('sheets', 'v4')

    def get_headers_row2(self):
        resp = self.sheets_api.spreadsheets().values().get(
            spreadsheetId=self.sheet_id,
            range="Лист1!2:2",
        ).execute()
        vals = resp.get("values", [[]])
        return vals[0]