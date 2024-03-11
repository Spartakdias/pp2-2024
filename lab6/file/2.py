import os

def check_path(path):
    try:
        if os.path.exists(path):
            print("Path exists")
        
            if os.access(path, os.R_OK):
                print("is readable.")
            else:
                print("is not readable")

            
            if os.access(path, os.W_OK):
                print("is writable")
            else:
                print("is not writable")

    
            if os.access(path, os.X_OK):
                print("is executable")
            else:
                print("is not executable.")

        else:
            print("does not exist")

    except Exception as e:
        print(f"{e}")
