import numpy as np


class Profile:
    def __init__(self, name, face_descriptors):
        """
        defines the Profile object's face descriptors

        Parameters
        ----------
        face_descriptors : np.ndarray
            512-dimensional vectors describing a face
        name : str
            name associated with the face
        """
        # add face descriptors
        self.face_descriptors = face_descriptors
        self.name = name
        self.mean_descriptor = 0

    def add_descriptor(self, descriptor):
        """
        add a face descriptor vector to the Profile's collection

        Parameters
        ----------
        descriptor : np.ndarray
            vector that describes a face
        """
        self.face_descriptors = self.face_descriptors.append(descriptor)

    def calculate_mean(self):
        """
        calculates mean descriptor for face
        """
        # calculate mean descriptor
        self.mean_descriptor = np.mean(self.face_descriptors)