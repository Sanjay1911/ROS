import rospy
import sys
import numpy as np
import math
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState

#initialise the ROS NODE
rospy.init_node('forward kinematics',anonymous=True)

#create a publisher object to publish the output
pub = rospy.Publisher('forward_kinematics_output',Float64MultiArray, queue_size=10)

#link parameters
a1 = 10
a2 = 10
a3 = 5
a4 = 10

#joint variables
d1 = 5
T2 = 30
T3 = -45

#degree to radian
T2=(T2/180.0)*np.pi
T3=(T3/180.0)*np.pi

#table (theta,alpha,r,d)
PT = [[(0.0/180.0*np.pi),(0.0/180.0*np.pi),0,a1+d1],
      [T2,(0.0/180.0*np.pi),a2,0],
      [T3,(0.0/180.0*np.pi),a4,a3]]



#Homo Trans Matrix
i=0
H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
i=1
H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
i=2
H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

H0_1 = np.matrix(H0_1)
print("H0_1")
print(H0_1)

H1_2 = np.matrix(H1_2)
print("H1_2")
print(H1_2)

H2_3 = np.matrix(H2_3)
print("H2_3")
print(H2_3)

if __name__=='main':
    try:
        pub.publish(H0_1)
        pub.publish(H1_2)
        pub.publish(H2_3)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass