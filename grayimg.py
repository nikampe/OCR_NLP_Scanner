# functions for gray
from skimage import color
from scipy.fftpack import dct, idct


def grayimg(image):
    # converting picture to gray
    gray = color.rgb2gray(image)

    frequencies = dct(dct(gray, axis=0), axis=1)
    frequencies[:2,:2] = 0
    gray = idct(idct(frequencies, axis=1), axis=0)

    gray = (gray - gray.min()) / (gray.max() - gray.min()) # renormalize to range [0:1]
    return gray

    #imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test1.jpeg", img_as_ubyte(gray))