import os

def list_directories_files(path):
    try:
        entries = os.listdir(path)
        directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        print(directories)

        files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
        print(files)

        print(entries)

    except FileNotFoundError:
        print("path not found.")
    except Exception as e:
        print(f"{e}")

