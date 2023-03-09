from os import path
import sys
import pandas as pd
# argv.py
class DataInput:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    # all extensions supported by this project.
    supported_file_extensions = [
        '.csv',
    ]

    # function to convert all the column names of any specific dataset into lowercase.
    def change_to_lower_case(self, data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
        return data

    # function that takes any dataset from the input file and convert it into DataFrame.
    # The print statements are well defined and tells about the state of the errors.
    def inputFunction(self):
        import pandas as pd

class DataInput:

    def __init__(self):
        pass

    def inputFunction(self):
        filename = input("Enter file name without extension: ")
        file_extension = input("Enter file extension: ")
        encoding_type = 'GB18030'  # specify the byte order explicitly as little-endian UTF-16
        try:
            data = pd.read_csv(filename + file_extension, encoding=encoding_type)
            return data
        except Exception as e:
            print(str(e))
