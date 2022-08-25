#Main project

import os
import time
import colorama
from colorama import Fore, Back, Style
from exiftool import ExifToolHelper

#https://sylikc.github.io/pyexiftool/examples.html      pyexiftool api

def exif_tool():
    exif_input = input("Please enter the full directory of the file you want to extract from: ") #Examples can be "/Users" or "/yourname"
    with ExifToolHelper() as et:
        for d in et.get_metadata(str(exif_input)):
            for k, v in d.items():       #k = key , v = value
                print(f"Type: {k} = {v}")  #formatting as a dictionary

def list_directory(usr_input): 
    for i in os.listdir(usr_input):
        if i.endswith(".jpg"):
            my_list.append(i)
        elif i.endswith(".pdf"):
            my_list.append(i)
        elif i.endswith(".txt"):
            my_list.append(i)
        elif i.endswith(".png"):
            my_list.append(i)
    print(Fore.BLUE + str(my_list))
    
def main():
    print("".join(("=",)*40))
    print("".join(("+",)*40))
    print("".join(("=",)*40))
    
    print("This is your current directory you are in: " + os.getcwd())
    usr_input = input("Please enter directory to search for files:  ")
    list_directory(usr_input)
    while True: 
        cont_input = input("Do you wish to go further into the directory? (y/n): ")
        if(cont_input.upper() == "Y"):
            usr_input = input("Please enter directory to search for files:  ")
            list_directory(usr_input)
        elif(cont_input.upper() == "N"):
            #list_directory(usr_input)
            break
    exif_tool()
    

main()
