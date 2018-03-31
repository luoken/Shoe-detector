import numpy as np
import cv2

class Preprocessor():

    def __init__(self):
        self.preprocessor_queue = [] # sb a queue instead?
        self.preprocessor_output = [] # store each preprocess output
        self.pp_list = {} # maybe dict instead?
        self.roi = []

    def add_preprocess(self, preprocess):
        self.preprocessor_queue.append(preprocess)

    def get_preprocessor_queue(self):
        return self.preprocessor_queue

    # loop and run each preprocess
    def run(self):
        for process in self.preprocessor_queue:
            self.preprocessor_output.append(process.get_output() )
