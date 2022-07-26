import pikepdf
from PIL import Image
from PIL.ExifTags import TAGS
import os
import time
#i have made this change 
def pdf_extract():
    pdf_input = input("Please enter the pdf you want to extract from: ")#test cases 'cover_letter.pdf'
    pdf = pikepdf.Pdf.open(pdf_input)
    pdf_info = pdf.docinfo
    for key, value in pdf_info.items():
        print(key , ':' , value)

def image_extract():
    #Note: Images you wish to extract should be at the same local folder of this program

    #To find full directory of an image type in the following in the terminal:  
    #Linux: find "$(cd..;pwd)" -name "filename"
    image_input = input("Please enter the full directory of the image you want to extract from: ")
    image = Image.open(str(image_input))
    
    exif_data = image.getexif()


    for tagid in exif_data:
        tag_name = TAGS.get(tagid, tagid)
        value = exif_data.get(tagid)
        print(f"{tag_name:25}: {value}" )

def list_directory(dir_input):
    my_stack = []
    print(os.listdir(dir_input))

    


def main():
    print("".join(("=",)*40))
    print("".join(("+",)*40))
    print("".join(("=",)*40))
    
    #my_stack = []
    print("This is your current directory you are in: " + os.getcwd())
    user_input = input("Please enter (P) if you wish to extract data from pdf or (I) to extract data from images: ")
    if(user_input == "P"):
        dir_input = input("Please enter directory to search for files: ")
        list_directory(dir_input)
        while True:
            cont_input = input("Do you wish to go further into a specific directory?(y/n): ")
            if(cont_input == "y"):
                #my_stack.append(dir_input)
                #print("This is your directory so far: " + my_stack)
                dir_input = input("Please enter FULL directory to search for files: ")
                list_directory(dir_input)
            elif(cont_input == "n"):
                break
        pdf_extract()
        
    elif(user_input == "I"):
        dir_input = input("Please enter directory to search for files (I can list out all directories, i.e /home): ")
        list_directory(dir_input)
        while True:
            cont_input = input("Do you wish to go further into a specific directory?(y/n): ")
            if(cont_input == "y"):
                
                dir_input = input("Please enter directory to search for files: ")
                list_directory(dir_input)
            elif(cont_input == "n"):
                break
        image_extract()
main()
