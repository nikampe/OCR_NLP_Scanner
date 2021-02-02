import time
import cv2
import pytesseract
#from pytesseract import Output
import spacy

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
#custom_config2 = r'-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzäöüABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ.:€'

# Test 1 with all versions - Best results: 1 and 2
# Test 2 with all versions - Best results: 2 and 3
# Test 3 without preprocessing: Works surprisingly well but saves no significant time
def preprocessing1(receipt_path, output_path_preprocessed):
    # Read Image
    receipt = cv2.cvtColor(cv2.imread(receipt_path), cv2.COLOR_BGR2RGB)
    # Grayscale
    receipt_processed = cv2.cvtColor(receipt, cv2.COLOR_RGB2GRAY)
    # Gaussian blur
    receipt_processed2 = cv2.GaussianBlur(receipt_processed, (5, 5), 0)
    # Threshold
    receipt_processed3 = cv2.adaptiveThreshold(
        receipt_processed2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15
        )
    # Write Image
    cv2.imwrite(output_path_preprocessed, receipt_processed3)

def preprocessing2(receipt_path, output_path_preprocessed):
    # Read Image
    receipt = cv2.cvtColor(cv2.imread(receipt_path), cv2.COLOR_BGR2RGB)
    # Grayscale
    receipt_processed = cv2.cvtColor(receipt, cv2.COLOR_RGB2GRAY)
    # Gaussian blur
    receipt_processed2 = cv2.GaussianBlur(receipt_processed, (5, 5), 0)
    # Threshold
    receipt_processed3 = cv2.adaptiveThreshold(
        receipt_processed2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 30
        )
    # Write Image
    cv2.imwrite(output_path_preprocessed, receipt_processed3)    

def preprocessing3(receipt_path, output_path_preprocessed):
    # Read Image
    receipt = cv2.cvtColor(cv2.imread(receipt_path), cv2.COLOR_BGR2RGB)
    # Grayscale
    receipt_processed = cv2.cvtColor(receipt, cv2.COLOR_RGB2GRAY)
    # Gaussian blur
    receipt_processed2 = cv2.GaussianBlur(receipt_processed, (5, 5), 0)
    # Threshold
    receipt_processed3 = cv2.adaptiveThreshold(
        receipt_processed2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 30
        )
    # Write Image
    cv2.imwrite(output_path_preprocessed, receipt_processed3)


def result_into_txt(output_path_preprocessed, image_no, variant):
    result = pytesseract.image_to_string(output_path_preprocessed, lang="deu", config=custom_config)
    #result_encoded = str(result.encode("utf-8"))
    #file_1 = open("C:\\Users\\victo\\nlp1\\Examples\\Texts\\" + str(image_no) + "_" + str(variant) + ".json", "w")
    #file_1.write(result)
    #file_1.close()
    print("Result of Image " + str(image_no) + " and Variant " + str(variant) + ":")
    print("")
    print(result)
    print("-----------------------------------------------------------")

print("Main OCR function was initialized.")
n = 2

for i in range(1, n):
    print("Picture " + str(i))
    receipt_path = r"C:\\Users\\victo\\nlp1\\Examples\\Testing1\\" + str(i) + ".jpg"
    #output_path_preprocessed1 = r"C:\\Users\\victo\\nlp1\\Examples\\Preprocessing\\" + str(i) + "_1.jpg"
    output_path_preprocessed2 = r"C:\\Users\\victo\\nlp1\\Examples\\Preprocessing\\" + str(i) + ".jpg"
    #output_path_preprocessed3 = r"C:\\Users\\victo\\nlp1\\Examples\\Preprocessing\\" + str(i) + "_3.jpg"
    #preprocessing1(receipt_path, output_path_preprocessed1)
    preprocessing2(receipt_path, output_path_preprocessed2)
    #preprocessing3(receipt_path, output_path_preprocessed3)
    #result_into_txt(output_path_preprocessed1, i, 1)
    result_into_txt(output_path_preprocessed2, i, 2)
    #result_into_txt(output_path_preprocessed3, i, 3)