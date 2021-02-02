from finalpreprocessing import preprocessing
# conditions
    # contrast between receipt and background
    # relatively straight image of the receipt, only slightly turned
import imageio
# OCR function --> tesseract wrapper
import pytesseract as tess

import spacy
from spacy.matcher import Matcher

# loading spacy model
nlp = spacy.load("de_core_news_sm")
# Where to find the tesseract
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# matcher initialisieren
currency_matcher = Matcher(nlp.vocab)

def finder(doc, matcher):
    matches = matcher(doc)
    if len(matches) > 0:
        return True
    return False

#Währungssymbole
pattern_currency1 = [{'IS_CURRENCY': True}]
pattern_currency2 = [{'LOWER': {'IN': ["euro", "eur", "chf", "sfr"]}}]

currency_matcher.add("CURRENCY", None, pattern_currency1, pattern_currency2)

# Dieses Bild muss dann bereits zugeschnitten sein.
image = imageio.imread(r"C:\\Users\\victo\\nlp1\\Examples\\test.jpeg")

receipt = preprocessing(image)

# receiving the text from the image
custom_config = r'-c preserve_interword_space=1 --oem 1 --psm 4 --dpi 96'

text = tess.image_to_string(receipt, lang='deu', config=custom_config)

doc = nlp(text)
print(finder(doc, currency_matcher))




# further updates:

    # adding reoccuring words to the tesseract dictionary
    # whitelist characters
    # # Configuration of the tesseract:
        # oem 1: Use LSTM only
        # psm 4: Assume a single column of text of variable sizes
        # interword spaces prevents textelements to be printed together
        # character whitelist: only characters available to detect and print
        # dpi 72 --> custom dpi of iPhone --> helps the tesseract to detect pixels --> after the preprocessing of the pictures we arrive at 96 dpi
            # custom_config = r'-c preserve_interword_space=1 --oem 1 --psm 4 --dpi 72'
