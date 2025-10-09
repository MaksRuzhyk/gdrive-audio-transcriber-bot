from source.drive_calls import DriveCalls
from source.transcription.whisper_transcriber import Whisper
from source.google_tables.sheets_client import SheetsClient

def main():
    dc = DriveCalls()
    files = dc.get_list_calls()
    print(f'Список дзвінків: {files}, {len(files)} файлів.')
    paths = dc.download_all_calls()
    print(f'Завантажено: {len(paths)}')

    # transcriber = Whisper()
    #
    # for p in paths:
    #     print('Run...')
    #     print(p)
    #     text = transcriber.transcribe(str(p))
    #     print('-' * 100)
    #     print(text)
    #     print('-' * 100)

    sheets = SheetsClient()
    info = sheets.get_headers_row2()
    print(info)

if __name__ == '__main__':
    main()