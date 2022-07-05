#! /usr/bin/env python
import sys
import rospy
from alphabet_sorter.srv import sort_stringMessage, sort_stringMessageRequest
from std_msgs.msg import String



def client_callback(msg):
#Once a message is published in the /input topic the client_callback method 
#sends it to the sorter service server to sort and publish the output
    msg=str(msg) #convert to string
    sorter_service_object=msg # set the service message Request
    result=sorter_service(sorter_service_object) #call the service with the new input


#initialize the service-client node
rospy.init_node('sorter_service_client')
rospy.wait_for_service('/sorter_service') #wait for the service to be active
sorter_service=rospy.ServiceProxy('/sorter_service',sort_stringMessage) #connect to the service
sorter_service_object=sort_stringMessageRequest
# subscribe to the /input topic as mentioned in the task
sub=rospy.Subscriber('/input',String, client_callback)
rospy.spin() #keep the program active

