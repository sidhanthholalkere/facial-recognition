from cosdist import cosine_dist
import numpy as np

def cosdist_to_adjmatrix(picture_descriptors, cutoff):
    """

    Parameters
    ----------
    picture_descriptors : shape(N,) numpy.ndarray
        numpy array of the descriptors of the pictures
    cutoff : float value determined by experimentation
        determines whether or not 2 nodes have a connection
        
    Returns
    -------
    adjacency_matrix : shape (N, N) np.ndarray containing weighted cosine distances
    """
    adjacency_matrix = np.zeros(picture_descriptors.shape[0] ** 2)
    adjacency_matrix = adjacency_matrix.reshape(picture_descriptors.shape[0], picture_descriptors.shape[0])
    for i in range(adjacency_matrix.shape[0]):
        for j in range(adjacency_matrix.shape[1]):
            if cosine_dist(picture_descriptors[i], picture_descriptors[j]) < cutoff:
                adjacency_matrix[i][j] = 1/(cosine_dist(picture_descriptors[i], picture_descriptors[j]) ** 2)
    return adjacency_matrix