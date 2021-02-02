#import time
#import cv2
import pytesseract
#from pytesseract import Output
import spacy
from Preprocessing import preprocessing2

# NLP-Modell laden
nlp = spacy.load("de_core_news_sm")

# Where to find the tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configuration of the tesseract
    # oem 1: Use LSTM only
    # psm 4: Assume a single column of text of variable sizes
    # interword spaces prevents textelements to be printed together
    # character whitelist: only characters available to detect and print
    # dpi 72 --> custom dpi of iPhone --> helps the tesseract to detect pixels
custom_config = r'-c preserve_interword_space=1 --oem 1 --psm 4 --dpi 72'

n = 112

for i in range(111, n):
    print("------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------")
    print("Picture " + str(i))
    print("------------------------------------------------------------------------------------------------------------")
    receipt_path = r"C:\\Users\\victo\\nlp1\\Examples\\Testing1\\" + str(i) + ".jpg"
    output_path_preprocessed2 = r"C:\\Users\\victo\\nlp1\\Examples\\Preprocessing\\" + str(i) + ".jpg"
    preprocessing2(receipt_path, output_path_preprocessed2)
    result = pytesseract.image_to_string(output_path_preprocessed2, lang="deu", config=custom_config)
    print(result)
    doc = nlp(result)
    print([token.text for token in doc])
