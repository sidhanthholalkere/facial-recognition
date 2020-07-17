import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
from facenet_models import FacenetModel
import cv2

def descriptors_from_camera():
    """
    Generates descriptors for detected faces in an image
    from the camera

    Returns
    -------
    descriptor : np.ndarray
        Descriptors for the images
    """

    pic = take_picture()

    model = FacenetModel()

    boxes, probabilities, _ = model.detect(pic)

    descriptor = model.compute_descriptors(pic, boxes)

    return descriptor

def descriptors_from_img_path(path):
    """
    Generates descriptors for detected faces in an image
    from a file path
    
    Parameters
    ----------
    path: String
        path to image

    Returns
    -------
    descriptor : np.ndarray
        Descriptors for the images
    """
    img = cv2.imread(path)

    model = FacenetModel()

    boxes, probabilities, _ = model.detect(img)

    descriptor = model.compute_descriptors(img, boxes)

    return descriptor
