#Main project

import os
import time
from exiftool import ExifToolHelper

#https://sylikc.github.io/pyexiftool/examples.html      pyexiftool api

def exif_tool():
    exif_input = input("Please enter the full directory of the file you want to extract from: ")
    with ExifToolHelper() as et:
        for d in et.get_metadata(str(exif_input)):
            for k, v in d.items():
                print(f"Type: {k} = {v}")

def list_directory(usr_input): 
    print(os.listdir(usr_input))

def main():
    print("".join(("=",)*40))
    print("".join(("+",)*40))
    print("".join(("=",)*40))
    
    #my_stack = []
    print("This is your current directory you are in: " + os.getcwd())
    usr_input = input("Please enter directory to search for files:  ")
    list_directory(usr_input)
    while True: 
        cont_input = input("Do you wish to go further into the directory? (y/n): ")
        if(cont_input.upper() == "Y"):
            usr_input = input("Please enter directory to search for files:  ")
            list_directory(usr_input)
        elif(cont_input.upper() == "N"):
            list_directory(usr_input)
            break
    exif_tool()
    

main()
