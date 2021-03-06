import pickle
from .profile_class import Profile
from . import utils
from pathlib import Path
import numpy as np


class ProfileDatabase:
    """A database that stores the names and Profiles
    """

    def __init__(self):
        """Initializes a Profile database
        """
        # database is a dict with the person's name as the key
        # and Profile object as the value
        self.database = {}

    def add_profile(self, name, prof):
        """ Adds a profile to the database, takes in the name and
            Profile object
            -----
                name: String
                    name of the profile
                prof: Profile
                    profile object of the name
        """
        self.database[name] = prof
    
    def remove_profile(self, name):
        """ Removes a profile to the database, takes in the name/key
            -----
                name: String
                    name of the profile
        """
        if self.database.get(name) is not None:
            self.database.pop(name)

    def add_image_to_db(self, name):
        """ adds image taken from camera to database, given a name 
        (create a new profile if the name isn’t in the database, 
        otherwise add the image’s face descriptor vector to 
        the proper profile)
        -------
            name: String
                name of the face in the image
            img: Image

        """
        descriptor = utils.descriptors_from_camera()

        if self.database.get(name) is not None:
            prof = self.database.get(name)
            prof.add_descriptor(descriptor)
        else:
            prof = Profile(name, descriptor)

        self.add_profile(name, prof)

    def add_image_from_path_to_db(self, name, path):
        """ adds image taken from camera to database, given a name 
        (create a new profile if the name isn’t in the database, 
        otherwise add the image’s face descriptor vector to 
        the proper profile)
        -------
            name: String
                name of the face in the image
            img: Image

        """
        descriptor = utils.descriptors_from_img_path(path)

        if self.database.get(name) is not None:
            prof = self.database.get(name)
            prof.add_descriptor(descriptor)
        else:
            prof = Profile(name, descriptor)

        self.add_profile(name, prof)

    def match_descriptor(self, descriptor, threshold=0.5):
        """
        Determines which profile the descriptor matches

        Parameters
        ----------
        descriptor : np.ndarray
            512-d descriptor for the face

        threshold : float
            threshold for cosine similarity

        Returns
        -------
        str
            name of person it matches
        """
        distance = 1 # placeholders
        profile_obj = None
        descript_placehold = None

        for i, (k, v) in enumerate(self.database.items()):
            cos_dis = utils.cosine_dist(descriptor, v.mean_descriptor)
            print(cos_dis)
            if cos_dis <= threshold and cos_dis < distance:
                profile_obj = v
                distance = cos_dis
                descript_placehold = descriptor

        if profile_obj is not None:
            profile_obj.add_descriptor(descript_placehold)
            print(profile_obj.name)
            return profile_obj.name
        else:
            print('No match found')

    def load_database(self, path):
        """
        takes in the path of the database, and returns loaded database
        ----------
            path: String
                The path of the database
        Returns
        -------
            
        """
        # loads dictionary/database of Profiles
        path = "facial_recognition/" + path
        path = Path(path)
        with open(path, mode="rb") as opened_file:
            self.database = pickle.load(opened_file)

        # return 'file does not exist'

    def save_database(self, filename):
        """
        takes in the name of file you want to save to, pickles the database object and saves to that file
        ----------
            filename: String
                the name of the file
        """
        with open(filename, mode="wb") as opened_file:
            return pickle.dump(self.database, opened_file)

    def change_means_into_512arr(self):
        """ changes each profile mean bc too lazy to reload db
        """
        for i, (k, v) in enumerate(self.database.items()):
            print(v.mean_descriptor.shape)
