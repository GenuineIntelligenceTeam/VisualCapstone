from weighted_graph import WeightedGraph
import os
import matplotlib.image as mpimg
import numpy as np

from dlib_models import download_model, download_predictor, load_dlib_models
download_model()
download_predictor()
from dlib_models import models

load_dlib_models()
face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]

pics = os.listdir("./../images/")
print(mpimg.imread("./../images/ian1.png").shape)
image_data = np.vstack([mpimg.imread("./../images/" + pic) for pic in pics])
print(image_data.shape)