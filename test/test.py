import os
import unittest
import count
import cv2 as cv
import numpy as np

class LearningTest(unittest.TestCase):
    def test_reduce(self):
        src = np.array([[1.0,2.0,3.0]])
        dim = 1
        rtype = cv.REDUCE_MAX
        dst = np.array([])
        dtype = -1
        self.assertEqual(cv.reduce(src, dim, rtype, dst, dtype).tolist(), np.array([[3.0]]).tolist())

    def test_mog2(self):
        bsMOG2 = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
        self.assertTrue(True)

    def test_video_capture(self):
        video = cv.VideoCapture('../crowd_density/Data/vid4.avi')
        self.assertTrue(True)
