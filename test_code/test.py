from util.analysis_realtime import analysis
import cv2
import numpy as np

# Initializing
cap = cv2.VideoCapture(0)
ana = analysis()



if __name__ == "__main__":
    frame = cv2.imread('test.jpeg')
    bm = ana.detect_face(frame)
    cv2.imwrite('test_result.jpeg', bm)