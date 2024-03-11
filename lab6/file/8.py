import os
import stat

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print("File deleted")
            else:
                print("Unable to delete.")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"{e}")
