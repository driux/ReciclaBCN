from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
import os
import pandas as pd
import numpy as np

def load_cnn():
    # Initialize some learner
    path = Path(os.getcwd())/"data"
    tfms = get_transforms(do_flip=True,flip_vert=True)
    data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16, num_workers=0)
    learn = cnn_learner(data,models.resnet34,metrics=error_rate)
    # Load previous trained model
    global MODEL
    MODEL = learn.load('trained_model')

# Predict from image
def predict(name):
    load_cnn()
    path2 = Path(os.path.abspath('static/tmp/'+name))
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


def get_result(img_src):
    # Devuelve el string que muestro por pantalla
    p = predict(img_src)
    if p[1] < 0.7:
        return 'negro'
    elif p[0] == 'cardboard':
        return 'azul'
    elif p[0] == 'glass':
        return 'verde'
    elif p[0] == 'metal' or p[0] == 'plastic':
        return 'amarillo'
    elif p[0] == 'trash':
        return 'negro'