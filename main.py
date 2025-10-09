from source.drive_calls import DriveCalls
from source.transcription.whisper_transcriber import Whisper

def main():
    dc = DriveCalls()
    files = dc.get_list_calls()
    print(f'Список дзвінків: {files}, {len(files)} файлів.')
    paths = dc.download_all_calls()
    print(f'Завантажено: {len(paths)}')

    transcriber = Whisper()

    for p in paths:
        print('Run...')
        print(p)
        text = transcriber.transcribe(str(p))
        print('-' * 100)
        print(text)
        print('-' * 100)


if __name__ == '__main__':
    main()