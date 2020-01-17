import numpy as np
import cv2
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split video frames into pictures for run ORBSLAM2 test')
    parser.add_argument('--video', type=str, required=True,
                        help='Input video file')
    parser.add_argument('--path', type=str, required=True,
                        help='Output frames folder')

    args = parser.parse_args()

    cap = cv2.VideoCapture(args.video)

    cntr = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        
        cv2.imshow('frame',frame)
        key = cv2.waitKey(0) & 0xFF 
        if key == ord('q'): 
            break
        if key == ord('s'): 
            cv2.imwrite(args.path+str(cntr)+'.png',frame) 
        cntr += 1
    cap.release()
    cv2.destroyAllWindows()
    
