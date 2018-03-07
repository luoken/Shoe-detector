import numpy as np
import cv2

class Task():
    
    def __init__(self):
        self.detector = None # definition later
        self.is_complete = False

    def is_task_complete(self):
        return self.is_complete

    def set_task_complete(self):
        self.is_complete = True

    def get_detector(self):
        return self.detector

    def __str__(self):
        pass


