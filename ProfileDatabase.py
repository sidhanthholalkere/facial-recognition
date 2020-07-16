import pickle
from pathlib import Path
import profile
import input
import cosdist

class ProfileDatabase:
    """A database that stores the names and Profiles
    """

    def __init__(self):
        """Initializes a Profile database
        """
        # database is a dict with the person's name as the key
        # and Profile object as the value
        self.database = {}

    def add_profile(self, name, profile):
        """ Adds a profile to the database, takes in the name and
            Profile object
            -----
                name: String
                    name of the profile
                profile: Profile
                    profile object of the name
        """
        self.database[name] = profile
    
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
        descriptor = input.descriptors_from_camera()

        if self.database.get(name) is not None:
            profile = self.database.get(name)
            profile.add_descriptor(descriptor)
        else:
            profile = profile.Profile(name, descriptor)

        self.add_profile(name, profile)

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
        descriptor = input.descriptors_from_img_path(path)

        if self.database.get(name) is not None:
            profile = self.database.get(name)
            profile.add_descriptor(descriptor)
        else:
            profile = profile.Profile(name, descriptor)

        self.add_profile(name, profile)

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
        for i, (k, v) in enumerate(self.database.items()):
            print(v.mean_descriptor.shape)
            if cosdist.cosine_dist(descriptor, v.mean_descriptor) <= threshold:
                v.add_descriptor(descriptor)
                return v.name

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
        path = Path(path)
        with open(path, mode="rb") as opened_file:
            self.database = pickle.load(opened_file)

        #return 'file does not exist'

    def save_database(self, filename):
        """
        takes in the name of file you want to save to, pickles the database object and saves to that file
        ----------
            filename: String
                the name of the file
        """
        with open(filename, mode="wb") as opened_file:
            return pickle.dump(self.database, opened_file)
