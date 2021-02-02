def polycandidates(corners):
    # initiating empty list of polygon candidates
    polygon_candidates = []
    # for every corner
    for corner1 in corners:
        # take another corner point starting with the first one
        # if x-value of corner 2 is more than x-value of corner 1
        for corner2 in corners:
            if corner2[0] > corner1[0]:
                # take another corner point starting with the first one
                # if y-value of corner 3 is less than y-value of corner 2
                for corner3 in corners:
                    if corner3[1] < corner2[1]:
                        # take another corner point starting with the first one
                        # if x-value is of corner 4 is less than x-va1lue of corner 3
                        # check if y-value of corner 4 is less than y-value of corner
                        for corner4 in corners:
                            # polygon candidate found
                            # add to array of polygon candidates
                            if corner4[0] < corner3[0] and corner4[1] < corner1[1]:
                                polygon_candidates.append([corner1, corner2, corner3, corner4])
    return polygon_candidates
