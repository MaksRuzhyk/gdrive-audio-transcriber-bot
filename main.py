from source.drive_calls import DriveCalls

def main():
    dc = DriveCalls()
    files = dc.get_list_calls()
    print(files)

if __name__ == '__main__':
    main()