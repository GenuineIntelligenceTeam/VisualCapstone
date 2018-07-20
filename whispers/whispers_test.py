from weighted_graph import WeightedGraph
import os
import matplotlib.image as mpimg
import numpy as np
import skimage.io as io

from dlib_models import download_model, download_predictor, load_dlib_models
download_model()
download_predictor()

def get_descriptor(img, face_detect, shape_predictor, fpath):
    detection = list(face_detect(img))[0]
    shape = shape_predictor(img, detection)
    descriptor = np.array(face_rec_model.compute_face_descriptor(img, shape))
    return descriptor

pics = os.listdir("./../images/")
image_data = [io.imread("./../images/" + pic) for pic in pics]

load_dlib_models()
from dlib_models import models
face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]

graph = WeightedGraph(get_descriptor(image, face_detect, shape_predictor, pics[i]) for i,image in enumerate(image_data))
print("Faces detected: " + str(graph.whispers_loop(1000)))

'''ian = []
casey = []
ashley =[]
for i in range(6):
    ian.append(np.ones(4) + 0.1*np.random.rand(4))
    casey.append(4 * np.ones(4) + 0.1*np.random.rand(4))
    ashley.append(9 * np.ones(4) + 0.1*np.random.rand(4))

graph = WeightedGraph(ian + casey + ashley)
print(ian + casey + ashley)
print(graph.whispers_loop(1000))'''
