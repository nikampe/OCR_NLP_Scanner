import numpy as np
from segmentdistance import distancePointSegment
from intersectioncheck import checkIntersections

def bestpolygon(array_polygon_candidates, verticalSegments, horizontalSegments, avg_x_vertical, avg_y_horizontal):
    # finding best polygon candidate --> lowest distance between segments found during edge detection and edges of the polygon candidate
    distance_list = []
    # for every candidate of polygons
    for candidate in array_polygon_candidates:
        # determine edge segments (vertical and horizontal)
        left_edge = np.array([candidate[0], candidate[3]])
        right_edge = np.array([candidate[1], candidate[2]])
        upper_edge = np.array([candidate[0], candidate[1]])
        lower_edge = np.array([candidate[3], candidate[2]])
        distance_to_segments = 0
        for verticalSegment in verticalSegments:
            # Problem: Es wird noch nicht der beste Polygon-Kandidat gefunden -- eventuell besser abstand zum start und endpunkt eines edge zu finden
            # if segments do not intersect --> find distance
            if not (checkIntersections(verticalSegment, left_edge) or checkIntersections(verticalSegment, right_edge)):
                # checking which edge corresponds to the segment
                if verticalSegment[0][0] < avg_x_vertical:
                    # distance is the shortest distance between every point and the other segment --> need to check for left and right edge because we do not know which one is closest to the segment
                    distances = [distancePointSegment(left_edge, verticalSegment[0]), distancePointSegment(left_edge, verticalSegment[1]), distancePointSegment(verticalSegment, left_edge[0]), distancePointSegment(verticalSegment, left_edge[1])]
                    distance_to_segments += min(distances)
                    # distance_to_segments += (distancePointSegment(left_edge, verticalSegment[0]) + distancePointSegment(left_edge, verticalSegment[1])
                else:
                    # distance is the shortest distance between every point and the other segment --> need to check for left and right edge because we do not know which one is closest to the segment
                    distances = [distancePointSegment(right_edge, verticalSegment[0]), distancePointSegment(right_edge, verticalSegment[1]), distancePointSegment(verticalSegment, right_edge[0]), distancePointSegment(verticalSegment, right_edge[1])]
                    distance_to_segments += min(distances)
            
        for horizontalSegment in horizontalSegments:
            if not (checkIntersections(horizontalSegment, upper_edge) or checkIntersections(horizontalSegment, lower_edge)):
                # checking which edge corresponds to the segment
                if horizontalSegment[0][1] < avg_y_horizontal:
                    # distance is the shortest distance between every point and the other segment --> need to check for upper and lower edge because we do not know which one is closest to the segment
                    distances = [distancePointSegment(lower_edge, horizontalSegment[0]), distancePointSegment(lower_edge, horizontalSegment[1]), distancePointSegment(horizontalSegment, lower_edge[0]), distancePointSegment(horizontalSegment, lower_edge[1])]
                    distance_to_segments += min(distances)
                else:
                    # distance is the shortest distance between every point and the other segment --> need to check for upper and lower edge because we do not know which one is closest to the segment
                    distances = [distancePointSegment(upper_edge, horizontalSegment[0]), distancePointSegment(upper_edge, horizontalSegment[1]), distancePointSegment(horizontalSegment, upper_edge[0]), distancePointSegment(horizontalSegment, upper_edge[1])]
                    distance_to_segments += min(distances)   
        # add up all saved differences for every candidate in a new list
        distance_list.append(distance_to_segments)

    # find position minimum of list --> position of best polygon
    best_polygon_position = distance_list.index(min(distance_list))
    coordinates = array_polygon_candidates[best_polygon_position]
    return coordinates