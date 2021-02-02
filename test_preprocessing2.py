import time

# conditions
    # contrast between receipt and background
    # relatively straight image of the receipt, only slightly turned
import numpy as np
import imageio
from skimage import img_as_uint, io, img_as_ubyte
# functions for gray
from skimage import color
from scipy.fftpack import dct, idct
# functions for edge detection
from skimage import filters, morphology, measure
from scipy.ndimage.morphology import binary_fill_holes
# functions for corner detection
from skimage import transform as tf
from Intersections import lineIntersections
from sklearn import cluster 
# function for determining best possible polygon
from intersectioncheck import checkIntersections
from segmentdistance import distancePointSegment
# functions for skewing and cropping
from scipy.spatial import distance
# functions for final noise reduction and border cleaning of cropped images
from skimage.segmentation import clear_border
# OCR function --> tesseract wrapper
import pytesseract as tess
# filtering confidence values --> dataframes necessary
import pandas
start1 = time.time()
# Where to find the tesseract
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# converting picture to gray
img = imageio.imread(r"C:\\Users\\victo\\nlp1\\Examples\\test.jpeg")
gray = color.rgb2gray(img)

frequencies = dct(dct(gray, axis=0), axis=1)
frequencies[:2,:2] = 0
gray = idct(idct(frequencies, axis=1), axis=0)

gray = (gray - gray.min()) / (gray.max() - gray.min()) # renormalize to range [0:1]

#imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test1.jpeg", img_as_ubyte(gray))

# receipt detection
mask = filters.gaussian(gray, 2) > 0.6
mask = morphology.binary_closing(mask, selem=morphology.disk(2, bool))
mask = binary_fill_holes(mask, structure=morphology.disk(3, bool))
mask = measure.label(mask)
mask = (mask == 1 + np.argmax([r.filled_area for r in measure.regionprops(mask)]))

edges = mask ^ morphology.binary_erosion(mask, selem=morphology.disk(2, bool))

#imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test2.jpeg", img_as_ubyte(mask))

edgecandidates = np.where(edges)
listofedge = list(zip(edgecandidates[0], edgecandidates[1]))
print(edgecandidates)
print(listofedge)
print(len(listofedge))



corner_candidates = []

#for height in range(mask.shape[0]):
#    for width in range(mask.shape[1]):
#        if mask[height][width]:
#            if mask[height - 1][width] and mask[height][width + 1] and mask[height - 1][width + 1] and mask[height + 1][width + 1] and mask[height + 1][width] and mask[height][width - 1] and mask[height - 1][width - 1] and mask[height + 1][width - 1]:
#                sorrounding_array = mask[height - 2: height + 3, width - 2: width + 3]
#                white_counter = np.count_nonzero(sorrounding_array == True)
#                receipt_share = white_counter / 25
#                if receipt_share < 0.4:
#                    corner_candidate = np.array([height + 1, width + 1])
#                    corner_candidates.append(corner_candidate)

#print(type(corner_candidates))
#print(len(corner_candidates)) 

# new idea for corner detection: 
    # take every white pixel of the mask that neighbours at least one black pixel.
    # build 5x5 array with the white pixel in the middle
    # calculate relation of black and white pixels
    # edge --> 0.5/0.5
    # corner --> 0.25 white / 0.5 black
    # define corner candidates as an array