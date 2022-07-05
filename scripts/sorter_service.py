#! /usr/bin/env python
import sys
import rospy
import re
from alphabet_sorter.srv import sort_stringMessage, sort_stringMessageResponse
from std_srvs.srv import Empty, EmptyResponse
from std_msgs.msg import String

def callback(request):
#this callback is called each time client sends data to the server
    print('sorting',request.string_input)
    data=re.sub('[^a-zA-Z0-9]',' ',request.string_input[6:]).replace(" ","") #data preprocessing: strip unnecessary characters and spaces
    print(data)
    result=''.join(sorted(data)) #sort and join
    print('result after sorting:',result) #print result in the terminal
    pub.publish(result) #publish to the /output topic
    return True

#initialize the service-server node
rospy.init_node('alphabet_sorter')
pub=rospy.Publisher('/output',String,queue_size=1) #the output needs to be published to /ouput topic as mentioned in the task description
sorter_service=rospy.Service('/sorter_service',sort_stringMessage,callback) 
rospy.spin() #keep the program active
