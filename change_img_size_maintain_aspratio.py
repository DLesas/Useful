def change_img_size_maintain_aspratio(img, dim=50):
    '''
    :param img : image to change
    :param dim : desired dimensions for the width and height of image
    :return: new_img; new image with new dimension whilst maintaining aspect ratio of original image 
    (via padding by (0, 0, 0) values or by upsampling via open cv).
    '''
    cvimg = cv2.imread(img)
    width, height, channels = cvimg.shape
    if width >= height:
        div = math.ceil(width / dim)
    elif height > width:
        div = math.ceil(height / dim)
    new_width = int(width / div)
    new_height = int(height / div)
    width_dif = abs(new_width - dim)
    height_dif = abs(new_height - dim)
    extrawidthpad = 0
    extraheightpad = 0
    if (width_dif % 2) != 0:
        extrawidthpad = 1
    if (height_dif % 2) != 0:
        extraheightpad = 1
    width_pad = math.floor(width_dif / 2)
    height_pad = math.floor(height_dif / 2)
    special_height_pad = height_pad + extraheightpad
    special_width_pad = width_pad + extrawidthpad
    resized = cv2.resize(cvimg, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    new_img = cv2.copyMakeBorder(resized, special_height_pad , height_pad, special_width_pad, width_pad, cv2.BORDER_CONSTANT, None, (0, 0, 0))
    
    return new_img
