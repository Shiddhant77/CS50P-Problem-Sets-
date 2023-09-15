from fpdf import FPDF
from PIL import Image,ImageDraw,ImageFont

pdf = FPDF(orientation='P', format='A4') # creating the instance of fpdf and giving it format and orientation

def main():
    user_input = input("Enter your name here : ")
    pdf.add_page() # adding a pdf page
    pdf.set_font('Arial', style='B',size=30) # assigning the font to write to the page
    pdf.cell(200,55, "CS50 Shirtificate", ln=True, align='C') # writing the header and centring it to the middle
    image_width = 180
    image_height = 180

    image = Image.open('shirtificate1.png') # using PIL library to open the image

    draw = ImageDraw.Draw(image) # drawing, meaning trying to write inside the image
    font = ImageFont.truetype("arial.ttf", size= 25) # assigning font to write into the image
    x,y = 150,200 # giving diameter where to write inside of image
    text= f"{user_input} took CS50P" # want we ant to write
    text_color = (255,255,255) # giving the text (White)
    draw.text((x,y), text,fill=text_color,font=font) # drawing, writing inside the image, boundary,what we want to write, color and font
    image.save('newshirtificate.png') # saving the image
    pdf.image('newshirtificate.png',w=image_width,h=image_height,) # importing the image inside of pdf
    pdf.output("CS50shirt.pdf") # finishing the pdf and saving it





if __name__=="__main__":
    main()