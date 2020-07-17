from node_class import node
import numpy as np

def adjmatrix_to_nodes(adj_matrix, descriptor):
    """

    Parameters
    ----------
    adj_matrix : shape (N,N) numpy.ndarray that shows how close nodes are connected(the greater the number the closer
    the connection)
        connections are determined by cosine distance

    descriptor : shape (N,) list containing the descriptor array for each of the pictures

    Returns
    -------
    node_list : shape (N,) list containing all the nodes created from the adjacency matrix
    """
    node_list = []
    for i in range(adj_matrix.shape[0]):
        neighbors = []
        for j in range(adj_matrix.shape[1]):
            if adj_matrix[i][j] != 0:
                neighbors.append(j)
        node_list.append(node(i, neighbors, descriptor[i]))
    return node_list

def whispers(adj_matrix, descriptor):
    """
    changes the label aspect of the class node to create clusters

    see adjmatrix_to_nodes for parameters
    """
    node_list = adjmatrix_to_nodes(adj_matrix, descriptor)
    cnt = 0
    label_cnt = []
    while cnt<1000:
        rand_node_indx = np.random.randint(0, len(node_list))
        rand_node = node_list[rand_node_indx]
        freq = np.zeros(len(node_list))

        for i in range(len(rand_node.neighbors)):
            check_node = node_list[rand_node.neighbors[i]]
            freq[check_node.label] += adj_matrix[rand_node.id][rand_node.neighbors[i]]
        rand_node(node_list[np.argmax(freq)].label)

        alive_labels = []

        for test_node in node_list:
            if test_node.label not in alive_labels:
                alive_labels.append(test_node.label)
        label_cnt.append(len(alive_labels))

        if len(label_cnt)>3:
            if label_cnt[-1] == label_cnt[-2] and label_cnt[-2] == label_cnt[-3]:
                cnt += 1

    return node_list



