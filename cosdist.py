

def cosine_dist(d1, d2):

    """

    takes image and returns image with face in box/features highlighted
    
    Parameters
    ----------
    d1 : numpy array
    first d vector

    d2 : numpy array    
    2nd d vector

    
    Returns
    -------
    
    cosine distance of d1 and d2
    
    """
    return 1 - (np.dot(d1, d2)) / (np.linalg.norm(d1)* np.linalg.norm(d2))




