import math
import numpy as np

#testsegment = np.array([[10, 10], [9, 2]])
#testpoint = np.array([10,10])

#print(testpoint)
#print(testsegment)

def distancePointSegment(Segment, Point):
    
    # defining variables from the input arrays
    x = Point[0]
    y = Point[1]
    x1 = Segment[0][0]
    y1 = Segment[0][1]
    x2 = Segment[1][0]
    y2 = Segment[1][1]

    A = x - x1
    B = y - y1
    C = x2 - x1
    D = y2 - y1

    # dot product and length of the square
    dot = A * C + B * D
    len_sq = C * C + D * D

    # initialising parameter for case differences
    param = -1

    # in case of segment of length 0
    if len_sq != 0:
        param = dot / len_sq
    
    # differentiating between different parameter values
    if param < 0:
        xx = x1
        yy = y1
    
    elif param > 1:
        xx = x2
        yy = y2
    
    else:
        xx = x1 + param * C
        yy = y1 + param * D

    dx = x - xx
    dy = y - yy
    return math.sqrt(dx * dx + dy * dy)

#print(distancePointSegment(testsegment, testpoint))