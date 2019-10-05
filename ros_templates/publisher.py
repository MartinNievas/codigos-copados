#The ROS Node Publisher template
 
#!usr/bin/env python
 
#remove or add the library/libraries for ROS
import rospy, time, math, random
 
#remove or add the message type
from std_msgs.msg import Int32, Float32, String
from basics.msg import TimerAction, TimerGoal, TimeResult
from time import sleep
 
#you can define functions to provide the required functionality
def body(arg):
    def_body_here
    return the_value
 
if __name__=='__main__':
    #add here the node name. In ROS, nodes are unique named.
    rospy.init_node('THE_NAME_OF_THE_NODE')
 
    #publish messages to a topic using rospy.Publisher class
    name_pub=rospy.Publisher('THE_NAME_OF_THE_TOPIC', THE_TYPE_OF_THE_MESSAGE, queue_size=1)
 
    #you can define functions to provide the required functionality
    if var1==var2:
        make_something()
        else:
            make_something()
 
    #set a publishing rate. Below is a publishing rate of 10 times/second
    rate=rospy.Rate(10)
 
    while not rospy.is_shutdown():
        #some calculation here
        if a1==a2:
            pub.publish(message1)
            else:
                pub.publish(message2)
rate.sleep()
