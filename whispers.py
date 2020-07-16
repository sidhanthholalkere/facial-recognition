from node_class import node
import numpy as np

def adjmatrix_to_nodes(adj_matrix, descriptor):
    """

    Parameters
    ----------
    adj_matrix : shape (N,N) matrix of 0s and 1s that shows which nodes are connected
        connections are determined by cosine similarities

    descriptor : shape (N,) list containing the descriptor array for each of the pictures

    Returns
    -------
    node_list : shape (N,) list containing all the nodes created from the adjacency matrix
    """
    node_list = []
    for i in range(adj_matrix.shape[0]):
        neighbors = []
        for j in range(adj_matrix.shape[1]):
            if adj_matrix[i][j] == 1:
                neighbors.append(j)
        node_list.append(node(i, neighbors, descriptor[i]))
    return node_list

def whispers(adj_matrix, descriptor):
    """
    changes the label aspect of the class node to create clusters
    """
    node_list = adjmatrix_to_nodes(adj_matrix, descriptor)
    while(True):
        rand_node_indx = np.random.randint(0, node_list.shape[0])
        test_node = node_list[rand_node_indx]
        freq = np.zeros(node_list.shape[0], dtype=int)
        for i in range(len(test_node.neighbors)):
            freq[test_node.neighbors[i]] += 1
        test_node(np.argmax(freq))
        


