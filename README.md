## Налаштування

   ### 1. Створіть проєкт у Google Cloud

- Перейдіть: console.cloud.google.com → Select project → New Project → створіть.

   ### 2. Увімкніть потрібні API

- APIs & Services → Enable APIs and Services → знайдіть і Enable:
    
- Google Drive API
    
- Google Sheets API
    
   ### 3. Створіть Service Account
    
- APIs & Services → Credentials → Create Credentials → Service account.
    
- Дайте назву, створіть. Роль можна пропустити або поставити Editor.
    
   ### 4. Завантажте JSON-ключ
    
- Зайдіть у створений сервіс-акаунт → Keys → Add key → Create new key → JSON.
    
- Збережіть файл service_account.json у корінь проєкту (і додайте в .gitignore).
    
   ### 5. Надайте доступ до папки на Google Drive
    
- Відкрийте потрібну папку з дзвінками → Share/Поділитися.
    
- Додайте email сервіс-акаунта (вигляду …@…iam.gserviceaccount.com) з правом Viewer (або Editor, якщо плануєте запис/видалення).
    
- Якщо це Shared Drive, теж поділіться з цим email.
    
   ### 6. Скопіюйте ID папки
    
- В адресному рядку Drive після /folders/ — це ваш DRIVE_FOLDER_ID.

   ### 7. Створіть `.env` із шаблону
- Скопіюйте приклад і заповніть:
  - Windows (PowerShell): `copy .env.example .env`
  - macOS/Linux: `cp .env.example .env`
- У `.env` вкажіть:
  ```ini
  GOOGLE_APPLICATION_CREDENTIALS=C:/абсолютний/шлях/до/service_account.json
  DRIVE_FOLDER_ID=ваш_ID_папки
  DOWNLOAD_DIR=data/audio

## Старт
```bash
git clone <repo_url>
cd Transcription_bot
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

