# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 03:16:36 2020

@author: Ratan Singh
"""

from sklearn.externals import joblib
import numpy as np
from python_speech_features import mfcc
import scipy.io.wavfile as wav


class Detector(object):
    
    """
    Loads the model from Database
    """
    def __init__(self):
        self.__model = joblib.load('model//model_22_jul.pkl')
        
    
    """
    Audio Feature Extraction
    """    
    def __extractFeatures(self, name):
        (rate,sig) = wav.read(name)
        mfcc_feat = mfcc(sig,rate, nfft=2048)
        mfcc_feat = np.mean(mfcc_feat, axis = 0)
        return mfcc_feat

    """
    Argument : Path to Audio File
    ReturnType : Binary
    
    Predicts the category of sound
    1 : Chainsaw cutting trees
    0 : No Cutting of trees using chainsaw
    """
    def predict(self, audioPath):
        features  = self.__extractFeatures(audioPath)
        y_pred = self.__model.predict(features.reshape([1,-1]))
        return y_pred[0]
