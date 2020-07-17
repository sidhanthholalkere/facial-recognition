# import input
from .ProfileDatabase import *

DB = ProfileDatabase()

DB = DB.load_database("facialDB.pkl")

print(DB.database.keys())

#DB.add_image_from_path_to_db("Ines", "Images/Ines1.PNG")

#DB.add_image_from_path_to_db("Austin", "Images/Austin1.png")

#DB.add_image_from_path_to_db("Olivia", "Images/Olivia1.png")

#DB.add_image_from_path_to_db("Sid", "Images/Sid1.jpg")

#DB.save_database("facialDB.pkl")