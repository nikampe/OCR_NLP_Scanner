import numpy as np
from skimage import transform as tf
from scipy.spatial import distance

def skewandcrop(image, coordinates):

    d = distance.pdist(coordinates)
    w = int(max(d[0], d[5])) # = max(dist(p1, p2), dist(p3, p4))
    h = int(max(d[2], d[3])) # = max(dist(p1, p4), dist(p2, p3))
    destination_matrix = np.array([[0,h], [w,h], [w,0], [0,0]])
    #print(destination_matrix)
    source_matrix = coordinates

    tr = tf.ProjectiveTransform()
    tr.estimate(destination_matrix, source_matrix)
    receipt = tf.warp(image, tr, output_shape=(h, w), order=1, mode="reflect")
    return receipt