import numpy as np
import matplotlib.pyplot as plt
import cv2
from camera import take_picture
from matplotlib.patches import Rectangle
from facenet_models import FacenetModel

def cosine_dist(d1, d2):
    """
    takes 512 d vectors and returns cosine distance

    Parameters
    ----------
    d1 : numpy array
        first d vector
    d2 : numpy array    
        2nd d vector

    Returns
    -------
    float
        cosine distance of d1 and d2
    
    """
    return 1 - (np.dot(d1, d2)) / (np.linalg.norm(d1)* np.linalg.norm(d2))

def display_image(pic, model, database):
    """
    Takes image and returns image with face in box/features highlighted

    Parameters
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