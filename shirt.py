import os, sys
from PIL import Image,ImageOps

def main():
    first_file = sys.argv[1]
    second_file = sys.argv[2]
    a = file_input(first_file,second_file)
    edit_file(first_file,second_file)

def file_input(first_file,second_file):

    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too less command line arguments")

    else:
        file_extension = ['.jpg', '.jpeg', '.png']
        extension = os.path.splitext(first_file)[1] # it splits name and file extension [1] is there cause we want to check if the ext in there or not same for file 2
        extension2 = os.path.splitext(second_file)[1]
        if extension2.lower() not in file_extension:
            sys.exit("Please insert a valid extension")
        if extension2.lower() != extension.lower():
            sys.exit("Both file should have the same extension ")
    return first_file,second_file

def edit_file(first_file, second_file):
    try:
        shirt = Image.open("shirt.png")   # opened the shirt image
        new_image = Image.open(first_file) # opening the image where we want to overlap the shirt image
        image_cropped = ImageOps.fit(new_image,shirt.size) # resizing the new image so it matches the dimesions of shirt image (shirt.size) return width and height of shirt
        image_cropped.paste(shirt, mask=shirt) # pasting the shirt into the resized new image, mask is telling it only to paste what should be pasted, anything on the image
        # except the size of the shirt nothing should be pasted
        image_cropped.save(second_file) # saving the overlapped image into a separate image file

    except FileNotFoundError:
        sys.exit("File does not exists")
if __name__ == '__main__':
    main()