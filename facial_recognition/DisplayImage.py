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

    the plot with the squares and names on it, and Unknown if there is no match 
    
    """

    fig,ax = plt.subplots()

    ax.imshow(pic)

    boxes, probabilities, landmarks = model.detect(pic)

    
    for box, prob, landmark in zip(boxes, probabilities, landmarks):
        # draw the box on the screen
        ax.add_patch((Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red")))
        
        #crop out the face
        
        x_topleft = round(int(box[0]))
        y_topleft = round(int(box[1]))
        x_bottomright = round(int(box[2]))
        y_bottomright = round(int(box[3]))
    
    
        pic_face = pic[x_topleft: x_bottomright, y_topleft:y_bottomright, :] #picface is the face cropped,
        
        boxes_face, probabilities_face, _ = model.detect(pic_face)
        
        descriptor = model.compute_descriptors(pic_face, boxes_face)
        
        name =  database.match_descriptor(descriptor)

        if name != None:
            ax.text(box[0:1], box[1:2]-10, name, color="white")
        else:
             ax.text(box[0:1], box[1:2]-10, "Unknown", color="white")
        
    
    return(plt)






