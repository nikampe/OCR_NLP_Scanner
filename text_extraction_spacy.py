#import time
#import cv2
import pytesseract
#from pytesseract import Output
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from Preprocessing import preprocessing2

# NLP-Modell laden
nlp = spacy.load("de_core_news_sm")

# deutsche Städte in Liste zusammenstellen
with open(r"C:\\Users\\victo\\nlp1\\Cities.txt", encoding="utf-8") as f:
    cities = f.read().splitlines()

# Phrasematcher erstellen
# Patterns für den Phrasematcher aus Städteliste lesen und hinzufügen
phrasematcher = PhraseMatcher(nlp.vocab, attr="LOWER")
pattern_city = [nlp.make_doc(text) for text in cities]
phrasematcher.add("CITY", None, *pattern_city)

# Matcher erstellen
# PLZ Pattern erstellen und zum Matcher hinzufügen
matcher = Matcher(nlp.vocab)
pattern_PLZ = [{'SHAPE': 'dddd', 'LENGTH': 5}]
matcher.add("PLZ", None, pattern_PLZ)

# Where to find the tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configuration of the tesseract
    # oem 1: Use LSTM only
    # psm 4: Assume a single column of text of variable sizes
    # interword spaces prevents textelements to be printed together
    # character whitelist: only characters available to detect and print
    # dpi 72 --> custom dpi of iPhone --> helps the tesseract to detect pixels
custom_config = r'-c preserve_interword_space=1 --oem 1 --psm 4 --dpi 72'

output_path_preprocessed = r"C:\\Users\\victo\\nlp1\\Examples\\Preprocessing\\104.jpg"
receipt_path = r"C:\\Users\\victo\\nlp1\\Examples\\Testing1\\104.jpg"
preprocessing2(receipt_path, output_path_preprocessed)

result = pytesseract.image_to_string(output_path_preprocessed, lang="deu", config=custom_config)
print(result)

doc = nlp(result)
matches = matcher(doc)
city_matches = phrasematcher(doc)
print("_______________________")
print([token.text for token in doc])
print("City and PLZ Matcher:")

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(string_id, span.text)

for match_id, start, end in city_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(string_id, span.text)