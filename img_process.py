from PIL import Image, ImageFilter
import os


new_img = None

def image_processing(path, height, width, frmt, directory):
    img = Image.open(path)
    global new_img
    new_img = img.resize((height, width))
    #img.thumbnail((400,200))     #maintains the aspect ratio
    print('converted')
    if frmt == 'JPG':
        new_img.save(f'{directory}/img', 'jpeg')
    elif frmt == 'PNG':
        new_img.save(f'{directory}/img', 'png')
    elif frmt == 'BMP':
        new_img.save(f'{directory}/img', 'bmp')

    #new_img.save('/home/pratish/Desktop/test', 'jpeg')
    
    #print ('saved')