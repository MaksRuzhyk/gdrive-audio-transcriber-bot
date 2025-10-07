from source.drive_calls import DriveCalls

def main():
    dc = DriveCalls()
    files = dc.get_list_calls()
    print(f'Список дзвінків: {files}, {len(files)} файлів.')
    paths = dc.download_all_calls()
    print(f'Завантажено: {len(paths)}')

if __name__ == '__main__':
    main()