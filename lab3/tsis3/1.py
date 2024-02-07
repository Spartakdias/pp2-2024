class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter string: ")

    def printString(self):
        print(self.input_string.upper())


