def angle_between(coords1, coords2, coords3):
    '''
    :param coords1: coords of point 1 in (x, y) format
    :param coords2: coords of point 2 in (x, y) format
    :param coords3: coords of point 3 in (x, y) format
    :return: angle; angle between coords 1 and coords 3 using coords2 as a pivot
    '''
    lengthofx1 = (coords1[0] - coords2[0])**2
    lengthofy1 = (coords1[1] - coords2[1])**2
    lengthofx2 = (coords2[0] - coords3[0])**2
    lengthofy2 = (coords2[1] - coords3[1])**2
    lengthofx3 = (coords3[0] - coords1[0])**2
    lengthofy3 = (coords3[1] - coords1[1])**2
    lengthof1 = math.sqrt(lengthofx1 + lengthofy1)
    lengthof2 = math.sqrt(lengthofx2 + lengthofy2)
    lengthof3 = math.sqrt(lengthofx3 + lengthofy3)
    angle = np.degrees(math.acos(((lengthof1**2)+(lengthof2**2)-(lengthof3**2))/(2*lengthof1*lengthof2)))

    return angle
