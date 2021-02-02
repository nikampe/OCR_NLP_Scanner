from grayimg import grayimg
from receiptdetection import receiptdetection
from cornerdetection import cornerdetection
from polycandidates import polycandidates
from bestpolygon import bestpolygon
from skewandcrop import skewandcrop
from border import add_border

import numpy as np
import imageio
from skimage import img_as_ubyte, filters, morphology
# functions for corner detection
from skimage import transform as tf

# functions for final noise reduction and border cleaning of cropped images
from skimage.segmentation import clear_border

def preprocessing(image):
    #adding border
    #borderimage = add_border(image, border=20)

    #turning bw
    gray = grayimg(image)

    # receipt detection
    #mask = receiptdetection(gray)
    #imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test2.jpeg", img_as_ubyte(mask))

    # edge detection & creation of vertical and horizontal segments
    #edges = mask ^ morphology.binary_erosion(mask, selem=morphology.disk(2, bool))
    #segments = np.array(tf.probabilistic_hough_line(edges))
    #angles = np.array([np.abs(np.arctan2(a[1]-b[1], a[0]-b[0]) - np.pi/2) for a,b in segments])
    #verticalSegments = segments[angles < np.pi/4] 
    #horizontalSegments = segments[angles >= np.pi/4]

    #imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test3.jpeg", img_as_ubyte(edges))

    # detection of possible corners (all intersections of vertical and horizontal segments)
    #corners = cornerdetection(verticalSegments, horizontalSegments)

    #polygon_candidates = polycandidates(corners)
    #print(corners.shape)
    #print(len(polygon_candidates))
    #array_polygon_candidates = np.array(polygon_candidates)

    #sum_x_vertical = 0
    #sum_y_horizontal = 0
    #for verticalSegment in verticalSegments:
    #    sum_x_vertical += verticalSegment[0][0] + verticalSegment[1][0]

    #avg_x_vertical = sum_x_vertical / (len(verticalSegments) * 2)

    #for horizontalSegment in horizontalSegments:
    #    sum_y_horizontal += horizontalSegment[0][0] + horizontalSegment[1][0]

    #avg_y_horizontal = sum_y_horizontal / (len(horizontalSegments) * 2)

    #coordinates = bestpolygon(array_polygon_candidates, verticalSegments, horizontalSegments, avg_x_vertical, avg_y_horizontal)

    #skewing and cropping
    #receipt = skewandcrop(gray, coordinates)

    # final noise reduction and border cleaning + enhancing the contrast a last time
    t_sauvola = filters.threshold_sauvola(gray, window_size=35, k=0.1)
    mask2 = gray < t_sauvola
    mask2 = clear_border(mask2)
    #imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test6.jpeg", img_as_ubyte(mask2))
    mask2 = filters.gaussian(mask2, 0.5)
    #imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test7.jpeg", img_as_ubyte(mask2))
    receipt = 1 - (1 - gray) * mask2
    #imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test8.jpeg", img_as_ubyte(receipt))
    receipt = receipt**4
    #imageio.imwrite(r"C:\\Users\\victo\\nlp1\\Examples\\test9.jpeg", img_as_ubyte(receipt))
    return receipt