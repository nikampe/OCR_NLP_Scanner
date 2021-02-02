from PIL import Image

im = Image.open("C:\\Users\\victo\\nlp1\\Examples\\5.jpg")
print(im.info["dpi"])