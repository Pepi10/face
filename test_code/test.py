from util.analysis_realtime import analysis
import cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Initializing
cap = cv2.VideoCapture(0)
ana = analysis()



if __name__ == "__main__":
    frame = cv2.imread('test_1.jpeg')
    bm = ana.detect_face(frame)
    cv2.imwrite('test_1_result.jpeg', bm)