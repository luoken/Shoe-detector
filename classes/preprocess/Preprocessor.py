import numpy as np
import cv2

class Preprocessor():

    def __init__(self):
        self.preprocessor_list = [] # sb a queue instead?
        self.roi = []

    def add_preprocess(self, preprocess):
        self.preprocessor_list.append(preprocess)

    def get_preprocessor_list(self):
        return self.preprocessor_list

    # loop and run each preprocess
    def run(self):
        pass
