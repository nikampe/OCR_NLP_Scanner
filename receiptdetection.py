# functions for edge detection
from skimage import filters, morphology, measure
from scipy.ndimage.morphology import binary_fill_holes
import numpy as np

# receipt detection
def receiptdetection(image):
    mask = filters.gaussian(image, 2) > 0.6
    mask = morphology.binary_closing(mask, selem=morphology.disk(2, bool))
    mask = binary_fill_holes(mask, structure=morphology.disk(3, bool))
    mask = measure.label(mask)
    mask = (mask == 1 + np.argmax([r.filled_area for r in measure.regionprops(mask)]))
    return mask