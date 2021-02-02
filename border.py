from PIL import ImageOps, Image
import PIL
import imageio
 
 
def add_border(img, border):
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border)
        return bimg
    else:
        raise RuntimeError('Border is not an integer or tuple!')
 
image = Image.open('C:\\Users\\victo\\nlp1\\TrainingData\\Pictures\\receipt (1).jpeg')

borderimage = add_border(image, border=20)

borderimage = borderimage.save('C:\\Users\\victo\\nlp1\\TrainingData\\Pictures\\border.jpeg')