import numpy as np
#testv = np.array([[10, 10], [9, 2]])
#testh = np.array([[5, 5], [15, 6]])


# vertical and horizontal in this case are just the names of two segments, they do not have to be vertical or horizontal respectively
def checkIntersections(vertical, horizontal):
    x_vertical1 = vertical[0][0]
    y_vertical1 = vertical[0][1]
    x_vertical2 = vertical[1][0]
    y_vertical2 = vertical[1][1]

    x_horizontal1 = horizontal[0][0]
    y_horizontal1 = horizontal[0][1]
    x_horizontal2 = horizontal[1][0]
    y_horizontal2 = horizontal[1][1]

    # Preventing division by zero and detecting a zero distance if the x-values of both segments are the same --> two perfectly vertical segments
    if (x_vertical1 == x_vertical2):
        if (x_vertical1 == x_horizontal1) and (x_horizontal1 == x_horizontal2):
            return True
        elif x_vertical1 == x_horizontal1:
            if (y_horizontal1 > min(y_vertical1, y_vertical2)) and (y_horizontal1 < max(y_vertical1, y_vertical2)):
                return True
        elif x_vertical1 == x_horizontal2:
            if (y_horizontal2 > min(y_vertical1, y_vertical2)) and (y_horizontal2 < max(y_vertical1, y_vertical2)):
                return True
        return False
    
    if x_horizontal1 == x_horizontal2:
        if (x_horizontal1 == x_vertical1) and (x_vertical1 == x_vertical2):
            return True
        elif x_horizontal1 == x_vertical1:
            if (y_vertical1 > min(y_horizontal1, y_horizontal2)) and (y_vertical1 < max(y_horizontal1, y_horizontal2)):
                return True
        elif x_horizontal1 == x_vertical2:
            if (y_vertical2 > min(y_horizontal1, y_horizontal2)) and (y_vertical2 < max(y_horizontal1, y_horizontal2)):
                return True
        return False

    # x and y values of the intersection have to be in these intervals
    x_values = [x_vertical1, x_vertical2, x_horizontal1, x_horizontal2]
    y_values = [y_horizontal1, y_horizontal2, y_vertical1, y_vertical2]
    x_values.remove(max(x_values))
    x_values.remove(min(x_values))
    y_values.remove(max(y_values))
    y_values.remove(min(y_values))
    
    slope_vertical = (y_vertical2 - y_vertical1)/(x_vertical2 - x_vertical1)
    add_vertical = y_vertical1 - (slope_vertical * x_vertical1)
    slope_horizontal = (y_horizontal2 - y_horizontal1)/(x_horizontal2 - x_horizontal1)
    add_horizontal =  y_horizontal1 - (slope_horizontal * x_horizontal1)

    # checking for parallel segments
    if slope_horizontal == slope_vertical:
        return False
    
    intersection_x = (add_horizontal - add_vertical)/(slope_vertical - slope_horizontal)

    # are the intersection coordinates part of the possible x and y values?
    if intersection_x > max(x_values) or intersection_x < min(x_values):
        return False

    return True
