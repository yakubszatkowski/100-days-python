import numpy as np
import cv2

class GameObject:
    def __init__(self, path):
        img = cv2.imread(path, 0)
        self.width = img.shape[1]
        self.height = img.shape[0]
        self.location = None
