from Intersections import lineIntersections
import numpy as np
# functions for corner detection
from skimage import transform as tf
from sklearn import cluster 

def cornerdetection(verticalSegments, horizontalSegments):
    intersections = [lineIntersections(vs, hs) for vs in verticalSegments for hs in horizontalSegments]
    intersections = np.array(intersections)
    # deleting irrelevant values (e.g. parallel segments) --> this unfortunately creates an one dimensional array
    nan_intersections = np.isnan(intersections)
    not_nan_intersections = ~ nan_intersections
    intersections_filtered = intersections[not_nan_intersections]

    # creating a new 2-dimensional array
    intersections_filtered_2d = np.reshape(intersections_filtered, ((int(intersections_filtered.size/2)), 2), order='C')
    #clustering the detected corner candidates into a managable amount // the higher the quantile, the less clusters (corners) are formed resulting in significantly less polygon candidates but also decreases quality of the best possible polygon
    bw = cluster.estimate_bandwidth(intersections_filtered_2d, quantile=0.15)
    corners = cluster.MeanShift(bandwidth=bw).fit(intersections_filtered_2d).cluster_centers_
    return corners