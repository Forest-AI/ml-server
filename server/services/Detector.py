# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 03:16:36 2020

@author: Ratan Singh
"""

import librosa
import joblib
import numpy as np

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
        try:
            audio, sample_rate = librosa.load(name, res_type = 'kaiser_fast')
            mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc = 40)
            mfccs_scaled = np.mean(mfccs.T, axis = 0)
        except Exception as e:
            print("Exception occurred in reading file {}".format(name))
            print(e)
            return None
        return mfccs_scaled


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
