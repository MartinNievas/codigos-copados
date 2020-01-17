#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import cv2
import time
from matplotlib import pyplot as plt
import numpy as np
import glob
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Aruco tags in pdf pages')
    parser.add_argument('--rows', type=int, required=True, default=5,
                        help='Number of inner rows. Default [5]')
    parser.add_argument('--cols', type=int, required=True, default=7,
                        help='Number of inner cols. Default [7]')
    parser.add_argument('--images', type=str, required=True,
                        help='Path to image folder')

    args = parser.parse_args()

    subpix_criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    #  calibration_flags = cv2.omnidir.CALIB_FIX_SKEW
    CHECKERBOARD = (args.rows,args.cols)
    objp = np.zeros((1, CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
    objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
    
    _img_shape = None
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    count = 0
    
    images = glob.glob(args.images+"*.png")

    for fname in images:
        print("Processing: "+fname)
        img = cv2.imread(fname)
        if _img_shape == None:
            _img_shape = img.shape[:2]
        else:
            assert _img_shape == img.shape[:2], "All images must share the same size."
    
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD,None, cv2.CALIB_CB_ADAPTIVE_THRESH+cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            cv2.cornerSubPix(gray,corners,(3,3),(-1,-1),subpix_criteria)
            imgpoints.append(corners)

    K = np.zeros((3, 3))
    D = np.zeros([1, 4])
    xi = np.zeros(1)
    calibration_flags = cv2.omnidir.CALIB_FIX_SKEW + cv2.omnidir.CALIB_USE_GUESS
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-6)
    rms = \
        cv2.omnidir.calibrate(
            objpoints,
            imgpoints,
            gray.shape[::-1],
            K,
            xi,
            D,
            calibration_flags,
            criteria)

    print(xi)
    #  print("Found " + str(N_OK) + " valid images for calibration")
    print("DIM=" + str(_img_shape[::-1]))
    print("K=np.array(" + str(K.tolist()) + ")")
    print("D=np.array(" + str(D.tolist()) + ")")
    
