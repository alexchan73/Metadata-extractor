
#Main project
import os
import time
import colorama
from colorama import Back, Fore, Style #Text with color package
from exiftool import ExifToolHelper #main meta data extraction package
from os import system, name
#https://sylikc.github.io/pyexiftool/examples.html
#have to install pyexiftool
def clear():
    if(name == 'nt'):
        _ = system('cls')
    else:
        _ = system('clear')

def exif_tool():
    exif_input = input("Please enter the full directory of the file you want to extract from: ")
    with ExifToolHelper() as et:
        for d in et.get_metadata(str(exif_input)):
            for k, v in d.items():
                print( Fore.MAGENTA + str(f"Info {k} = {v}"))

def list_directory(path_input):
    target_files = []
    folder_list = []
    idk_files = []
    for i in os.listdir(path_input):
        if i.endswith(".jpg"):
            target_files.append(i)
        elif i.endswith(".pdf"):
            target_files.append(i)
        elif i.endswith(".txt"):
            target_files.append(i)
        elif i.endswith(".png"):
            target_files.append(i)
        elif i.startswith("."):
            idk_files.append(i)
        elif os.path.isdir(path_input):
            folder_list.append(i)
    print(Fore.RED + str(target_files))
    print(Fore.YELLOW + str(folder_list))
    print(Fore.BLUE + str(idk_files))
    

def main():
    print(Fore.CYAN + "".join(("=",)*80))
    print(Fore.CYAN + "".join(("+",)*80))
    print(Fore.CYAN + "".join(("=",)*80))
    
    #my_stack = []
    print("This is your current directory you are in: " + os.getcwd())
    path_input = input("Please enter directory to search for files:  ")
    print("Red text is files that you can extract metadata from \nYellow text are folders/directories you can find other files \nBlue text is other files that starts with (.) ")
    list_directory(path_input)
    while True: 
        cont_input = input("Do you wish to go further into the directory? (y/n): ")
        if(cont_input.upper() == "Y"):
            clear()
            usr_input = input("Please enter directory to search for files:  ")
            list_directory(usr_input)
        elif(cont_input.upper() == "N"):
            break
    exif_tool()
main()
