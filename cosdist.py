

def cosine_dist(d1, d2):
    return 1 - (np.dot(d1, d2)) / (norm(d1)*norm(d2))
"""

    takes image and returns image with face in box/features highlighted
    
    Parameters
    ----------
    d1 : numpy array

    d2 : numpy array


    
    Returns
    -------
    
    ax, pic

    the ax and pic from the plot
    
    """



