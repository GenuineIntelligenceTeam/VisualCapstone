"""import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np

from dlib_models import download_model, download_predictor, load_dlib_models
download_model()
download_predictor()

pic = take_picture()

load_dlib_models()
from dlib_models import models
face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]

detections = list(face_detect(pic))
print(detections)"""

import sys
print(sys.path)