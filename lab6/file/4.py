def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(line_count)
    except FileNotFoundError:
        print("File is not found.")
    except Exception as e:
        print(f"{e}")