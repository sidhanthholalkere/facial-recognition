from facial_recognition.whispers import whispers
from facial_recognition.cosdist_to_adjmatrix import cosdist_to_adjmatrix
from facial_recognition.utils import descriptors_from_img_path
from pathlib import Path



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
    path = Path(file_path)
    for file in path.iterdir():
        file = file.resolve().as_posix()
        #print(descriptors_from_img_path(file).shape)
        descriptor_list.append(descriptors_from_img_path(file))

    threshold = 0.5 #update when value is confirmed

    adj_matrix = cosdist_to_adjmatrix(descriptor_list, threshold)
    node_list = whispers(adj_matrix, descriptor_list)
    return node_list

