import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
from matplotlib.patches import Rectangle


def display_image(pic, model, database):


    """

    takes image and returns image with face in box/features highlighted
    ----------
    pic : numpy array (length, width, 3(colours))
    picture you want to use

    model : FacenetModel()
    inited facenet model

    database: ProfileDatabase
    the database we are using
    
    Returns
    -------
    
    plt

    the plot with the squares on it 
    
    """

    fig,ax = plt.subplots()

    ax.imshow(pic)

    boxes, probabilities, landmarks = model.detect(pic)

    
    for box, prob, landmark in zip(boxes, probabilities, landmarks):
        print(box)
        # draw the box on the screen
        ax.add_patch((Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red")))
        ax.text(box[0:1], box[1:2]-10, "name", color="white")

    #query database for each face
    
    #use matplotlib to print the label
    
    return(plt)





