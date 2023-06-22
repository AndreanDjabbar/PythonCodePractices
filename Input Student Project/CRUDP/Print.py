import pandas
import os
from . import database

os.system("cls")

def print_data():
    
    data_pandas = pandas.read_csv(database.file_name)
    len_of_data = len(data_pandas)

    if len_of_data == 0:
        os.system("cls")
        print("Data Empty...")
        continue_program = input("Click Enter to continue: ")

    else:
        data_pandas = pandas.read_csv(database.file_name)
        file_target = input("Please input the name of file for print the data: ")
        file_target = f"{file_target}.txt"

        try:
            os.system("cls")
            with open(file_target, "w", encoding='utf-8') as f:
                f.write(str(data_pandas))
            print(f"\nData has been printed to \"{file_target}\"\n")
        except:
            print("\nError occurred\n")

