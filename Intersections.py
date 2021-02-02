import numpy as np
#testv = np.array([[10, 10], [9, 2]])
#testh = np.array([[5, 5], [15, 6]])

def lineIntersections(vertical, horizontal):
    x_vertical1 = vertical[0][0]
    y_vertical1 = vertical[0][1]
    x_vertical2 = vertical[1][0]
    y_vertical2 = vertical[1][1]

    x_horizontal1 = horizontal[0][0]
    y_horizontal1 = horizontal[0][1]
    x_horizontal2 = horizontal[1][0]
    y_horizontal2 = horizontal[1][1]

    # x and y values of the intersection have to be in these intervals
    x_values = [x_vertical1, x_vertical2, x_horizontal1, x_horizontal2]
    y_values = [y_horizontal1, y_horizontal2, y_vertical1, y_vertical2]
    x_values.remove(max(x_values))
    x_values.remove(min(x_values))
    y_values.remove(max(y_values))
    y_values.remove(min(y_values))

    # preventing division by 0
    if x_vertical1 == x_vertical2:
        intersection_x = np.nan
        intersection_y = np.nan
        return np.array([intersection_x, intersection_y])
    
    if x_horizontal1 == x_horizontal2:
        intersection_x = np.nan
        intersection_y = np.nan
        return np.array([intersection_x, intersection_y])

    slope_vertical = (y_vertical2 - y_vertical1)/(x_vertical2 - x_vertical1)
    add_vertical = y_vertical1 - (slope_vertical * x_vertical1)
    slope_horizontal = (y_horizontal2 - y_horizontal1)/(x_horizontal2 - x_horizontal1)
    add_horizontal =  y_horizontal1 - (slope_horizontal * x_horizontal1)

    # checking for parallel segments
    if slope_horizontal == slope_vertical:
        intersection_x = np.nan
        intersection_y = np.nan
        return np.array([intersection_x, intersection_y])
    
    intersection_x = (add_horizontal - add_vertical)/(slope_vertical - slope_horizontal)
    intersection_y = slope_vertical * intersection_x + add_vertical

    # are the intersection coordinates part of the possible x and y values?
    #if intersection_x > max(x_values) or intersection_x < min(x_values):
    #    intersection_x = np.nan
    #    intersection_y = np.nan
    #    return np.array([intersection_x, intersection_y])

    # getting rid of intersections that are outside the picture and therefore very unlikely corners
    if intersection_x < 0 or intersection_y < 0:
        intersection_x = np.nan
        intersection_y = np.nan
        return np.array([intersection_x, intersection_y])
    
    return np.array([intersection_x, intersection_y])