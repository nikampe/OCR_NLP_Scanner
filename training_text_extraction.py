
# conditions
    # contrast between receipt and background
    # relatively straight image of the receipt, only slightly turned
import imageio
from skimage import img_as_ubyte
# OCR function --> tesseract wrapper
import pytesseract as tess

from finalpreprocessing import preprocessing

# Where to find the tesseract
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

custom_config = r'-c preserve_interword_space=1 --oem 1 --psm 4 --dpi 96'


for i in range(7, 9):
    print("-------------------Picture " + str(i) + "--------------------")
    image = imageio.imread(r"C:\\Users\\victo\\nlp1\\TrainingData\\Pictures\\receipt (" + str(i) + ").jpeg")
    receipt = preprocessing(image)
    imageio.imwrite(r"C:\\Users\\victo\\nlp1\\TrainingData\\Pictures\\edit" + str(i) + ".jpeg", img_as_ubyte(receipt))
    text = tess.image_to_string(receipt, lang='deu', config=custom_config)
    print(text)



# further updates:

    # adding reoccuring words to the tesseract dictionary
    # whitelist characters
    # # Configuration of the tesseract:
        # oem 1: Use LSTM only
        # psm 4: Assume a single column of text of variable sizes
        # interword spaces prevents textelements to be printed together
        # character whitelist: only characters available to detect and print
        # dpi 72 --> custom dpi of iPhone --> helps the tesseract to detect pixels 
        # --> after the preprocessing of the pictures we arrive at 96 dpi
            # custom_config = r'-c preserve_interword_space=1 --oem 1 --psm 4 --dpi 72'
