import pikepdf
from PIL import Image
from PIL.ExifTags import TAGS
import os
import time
def pdf_extract():
    pdf_input = input("Please enter the pdf you want to extract from: ")#test cases 'cover_letter.pdf'
    pdf = pikepdf.Pdf.open(pdf_input)
    pdf_info = pdf.docinfo
    pdf_encrypt_info = pdf.encryption
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
    print(os.listdir(dir_input))

def main():
    print("")
    user_input = input("Please enter (P) if you wish to extract data from pdf or (I) to extract data from images: ")
    if(user_input == "P"):
        dir_input = input("Please enter directory to search for files: ")
        list_directory(dir_input)
        pdf_extract()
    elif(user_input == "I"):
        dir_input = input("Please enter directory to search for files: ")
        list_directory(dir_input)
        image_extract()
main()
