#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from opencv_features.srv import SavePos,SavePosResponse
from matplotlib import pyplot as plt
import numpy as np

array_of_features = []

class feature_cls():
    """Características"""
    def __init__(self, fture, pos):
        self.feature = fture
        self.pos = pos

    def get_feature(self):
        """"""
        return self.feature

    def get_pos(self):
        """"""
        return self.pos



class image_converter:

    def __init__(self):

        sim_camera_in = sys.argv[1]
        self.image_pub = rospy.Publisher("image_topic_2",Image)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber(str(sim_camera_in),Image,self.callback)
        self.vid_cod = cv2.VideoWriter_fourcc(*'XVID')
        self.output = cv2.VideoWriter("cam_video.mp4", self.vid_cod, 20.0, (800,800))

    def save_pos_callback(self,request):
        print("---------callback------------")
        return 1

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
          print(e)

        cv2.imshow("Image window", cv_image)
        self.output.write(cv_image)
        cv2.waitKey(1)

        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        except CvBridgeError as e:
            print(e)

def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

