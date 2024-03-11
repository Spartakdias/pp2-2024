import os
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_path = f"{letter}.txt"
        try:
            with open(file_path, 'w') as file:
                file.write(file_path)
            print("File created")
        except Exception as e:
            print(f"{e}")