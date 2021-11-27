# Importing libraries
import os
from PIL import Image

# The resulting pdf file
pdf_filename = "./output.pdf"

# Getting the images folder
folder_path = input('Enter the folder path: ')
my_list = os.listdir(folder_path)

# Converting the images in the folder to pdf
img1 = Image.open(folder_path + '/' + my_list[0])
img1.save(r'./output.pdf')

img_list = []

for i in my_list[1:]:
    # input_path = input('Enter the path: ')
    img = Image.open(folder_path + '/' + i)
    img_list.append(img)

img1.save(pdf_filename, "PDF", resolution=100.0,
          save_all=True, append_images=img_list)
