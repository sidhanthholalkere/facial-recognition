from facial_recognition import *
from facial_recognition import profile_class
import numpy as np
"""import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))"""

descriptors = utils.descriptors_from_camera()
new_profile = profile_class.Profile("Olivia", descriptors)
new_profile.add_descriptor(np.random.rand(1, 512))

populate_database.DB.add_image_to_db("Olivia")