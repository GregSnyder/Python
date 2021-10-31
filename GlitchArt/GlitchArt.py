from PIL import Image
import random

# Make sure JPEG is proper baseline formatted file
file_handler = open("/Users/gregorschneider/Desktop/Palazzo del Te/Template.jpg",'rb') # rb stands for reading binary mode
file_data = file_handler.read()
file_handler.close()

header_marker = b'\xff\xda' # 0xffd8 start of image and header, 0xffd9 end of image, but 0xffda start of scan and content
start_point = file_data.find(header_marker)+2
header_length = int(file_data[start_point:start_point+2].hex(),16)
start_point = start_point + header_length
ratio = 1
amount = round(len(file_data)/ratio)

for x in range(20):
    r = random.randint(0,amount)
    file_glitch = file_data[:start_point] + file_data[start_point+r:] #substract or add bytes to create glitch
    file_handler = open("/Users/gregorschneider/Desktop/Palazzo del Te/Glitch" + str(r) + ".jpg",'wb')
    file_handler.write(file_glitch)
    file_handler.close()
    im_glitch = Image.open("/Users/gregorschneider/Desktop/Palazzo del Te/Glitch" + str(r) + ".jpg")

print("header_marker:",header_marker,"header_length:", header_length)
print("byte-length original/glitch/amount: ",len(file_data),"/",len(file_glitch),"/",amount)
display(im_glitch)
