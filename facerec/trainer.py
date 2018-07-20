import os
import pickle
from collections import defaultdict
import numpy as np
from camera import take_picture
from dlib_models import download_model, download_predictor, load_dlib_models
download_model()
download_predictor()
from dlib_models import models
import skimage.io as io
import os
import matplotlib.pyplot as plt
from camera import take_picture
face_dict = defaultdict(np.array)
face_count = defaultdict(np.array)

load_dlib_models()
face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]

with open('database.pkl', 'rb') as handle: #Gets values of database and stores it in dictionary
    face_dict = pickle.load(handle)

print("Do you want to take a picture (0) or use a stored picture (1) for database?")
mode = int(input())
print("What is the name of the input face?")
person = input() #Gets the name of the face
if mode==0:
    print("Say cheese!")
    cheese = input()
    pic = take_picture()
    x = makedescriptors(pic)
    print(x)
    if x is None: #Skips if no face is detected to stop error
        print("Oof, I didn't see a face :(")
    else:
        LogPic(x,person)

elif mode==1:
    for i,filename in enumerate(os.listdir('.')): #Finds the images in directory that are .png and sets their descriptors for person
        if filename.endswith(".png"):
            x = uploadimage(filename)
            x = makedescriptors(x)
            if x is None: #Skips if no face is detected to stop error
                print(i)
                continue
            LogPic(x,person)
            continue
        else:
            continue
face_dict[person] = face_dict[person]/face_count[person] #Gets mean of the sum of images
with open('database.pkl', 'wb') as handle: #Packs new dictionary into database
    pickle.dump(face_dict, handle)