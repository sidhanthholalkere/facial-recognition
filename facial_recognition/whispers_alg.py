import whispers
from cosdist_to_adjmatrix import cosdist_to_adjmatrix
import utils
from os import listdir
from os.path import isfile, join


def whispers_alg(file_path):
    """
    reads in file path to folder containing images
    puts images through whisper algorithm and clusters images

    Parameters
    ----------
    file_path :  file path to a folder of images

    Returns
    -------
    node_list : list of nodes with labels clustering them into groups
    """

    descriptor_list = []
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles:
        descriptor_list.append(utils.descriptors_from_img_path(file))

    threshold = 0.5 #update when value is confirmed

    adj_matrix = cosdist_to_adjmatrix(descriptor_list, threshold)
    node_list = whispers(adj_matrix, descriptor_list)
    return node_list

