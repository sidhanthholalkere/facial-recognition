from facial_recognition.utils import cosine_dist
import numpy as np

def cosdist_to_adjmatrix(picture_descriptors, threshold):
    """

    Parameters
    ----------
    picture_descriptors : shape(N,) list of descriptors
        list of the descriptors of the pictures
    threshold : float value determined by experimentation
        determines whether or not 2 nodes have a connection
        
    Returns
    -------
    adjacency_matrix : shape (N, N) np.ndarray containing weighted cosine distances
    """
    adjacency_matrix = np.zeros(len(picture_descriptors) ** 2)
    adjacency_matrix = adjacency_matrix.reshape(len(picture_descriptors), len(picture_descriptors))
    for i in range(adjacency_matrix.shape[0]):
        for j in range(adjacency_matrix.shape[1]):
            if cosine_dist(picture_descriptors[i][0], picture_descriptors[j][0]) < threshold and i!=j:
                adjacency_matrix[i][j] = 1/(cosine_dist(picture_descriptors[i][0], picture_descriptors[j][0]) ** 2)
    #print(adjacency_matrix)
    return adjacency_matrix