#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Point
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import math

distance = None
pose = None

def toCoordinates(msg):
    global distance,pose
    distance = msg.x
    pose = msg.y

def main():
    rospy.init_node("coordinates")

    rospy.Subscriber("lidar", Point, toCoordinates)

    # plt.axis([-200,200,0,200])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1) 
    # plt.show()

    while not rospy.is_shutdown():

        try:
            # plt.scatter(x,y)
            ax.set_xlim(-50, 50)
            ax.set_ylim(-50, 50)
            x = distance * math.sin(pose * (3.14/180));
            y = distance * math.cos(pose * (3.14/180));
            ax.plot(y, x, marker='o')
            display(fig)    
            clear_output(wait = True)
            plt.pause(0.2)
            
        except Exception as e:
            print(e)

        # plt.show()


if __name__ == "__main__":
    main()
    
    
    



    
        



