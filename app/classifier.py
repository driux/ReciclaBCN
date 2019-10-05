from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
import os
import pandas as pd
import numpy as np

MODEL = None

def load_cnn():
    # Initialize some learner
    path = Path(os.getcwd())/"data"
    tfms = get_transforms(do_flip=True,flip_vert=True)
    data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16, num_workers=0)
    learn = cnn_learner(data,models.resnet34,metrics=error_rate)
    # Load previous trained model
    MODEL = learn.load('trained_model')

# Predict from image
def predict(name):
    path2 = Path(os.getcwd())/(name+'.jpg')
    img = open_image(path2)
    preds = MODEL.predict(img)
    clas = str(preds[0])
    if clas == 'cardboard':
        return (clas, float(preds[2][0]))
    elif clas == 'glass':
        return (clas, float(preds[2][1]))
    elif clas == 'metal':
        return (clas, float(preds[2][2]))
    elif clas == 'paper':
        return (clas, float(preds[2][3]))
    elif clas == 'plastic':
        return (clas, float(preds[2][4]))
    elif clas == 'trash':
        return (clas, float(preds[2][5]))
