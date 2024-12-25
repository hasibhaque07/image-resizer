from PIL import Image
import os

def resize(im, new_width):
    width, height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = im.resize((new_width, new_height))
    return resized_image

files = os.listdir("images")
# print(files)
extentions = ['jpg', 'jpeg', 'png', 'gif']
for file in files:
    ext = file.split(".")[-1]
    # print(ext)
    if ext in extentions:
        im = Image.open("images/"+file)
        im_resized = resize(im, 300)
        filepath = f"resize_images/folder1/{file}.jpg"
        im_resized.save(filepath)


# im = Image.open("images/car.jpg")
# print(im.size)
# im = im.resize((100, 80))
# im.show()

# im_resized = resize(im, 200)
# im_resized.show()