import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
from facenet_models import FacenetModel

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
