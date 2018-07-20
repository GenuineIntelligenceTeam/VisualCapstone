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
    print("found", fpath)
    shape = shape_predictor(img, detection)
    descriptor = np.array(face_rec_model.compute_face_descriptor(img, shape))
    return fpath, descriptor

pics = os.listdir("./../images/")
image_data = [io.imread("./../images/" + pic) for pic in pics]

load_dlib_models()
from dlib_models import models
face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]

graph = WeightedGraph(get_descriptor(image, face_detect, shape_predictor, pics[i]) for i,image in enumerate(image_data))
graph.whispers_loop(4)

for node in graph.nodes:
    print(node.ID, node.fpath)
