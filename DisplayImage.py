import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
from matplotlib.patches import Rectangle


def display_image(pic, model, square=True, landmark=True):


    """

    takes image and returns image with face in box/features highlighted
    ----------
    pic : numpy array (length, width, 3(colours))
    picture you want to use

    model : FacenetModel()
    inited facenet model

    square : boolean
    True if we want to show the square

    landmark : boolean
    True if we want to show landmarks
    
    Returns
    -------
    
    ax, pic

    the ax and pic from the plot
    
    """

    fig,ax = plt.subplots()

    ax.imshow(pic)

    boxes, probabilities, landmarks = model.detect(pic)


    
    for box, prob, landmark in zip(boxes, probabilities, landmarks):
        # draw the box on the screen
        ax.add_patch((Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red")))



    return(plt)





