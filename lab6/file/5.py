def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(file_path)
    except Exception as e:
        print(f"{e}")