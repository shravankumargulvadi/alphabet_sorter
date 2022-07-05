# Alphabet_Sorter_ROS

### Develoment Environment Details
 - Python Version 3.9.7
 - ROS Noetic


## Instructions for setting up the environment
1. cd to the src folder within your catkin workspace and clone this repo
2. run in terminal: catkin_make
3. run in terminal: source devel/setup.bash
4. roslaunch alphabet_sorter sorter_service_client.launch
5. open a new terminal and run: rostopic echo /output
6. run another new terminal and run: rostopic pub /input std_msgs/String 'enter any string here'
7. Results can be seen in terminal 1 and 2



## Brief on methodology
The program has a generic ROS services template with a service server 'sorter_service.py' and service client 'sorter_service_client.py'. Both have their respective 
launch files in the launch folder. The client launch file also launches the server, once launched the client waits for a string to be published in the /input topic
and once published it sends the message across to the server to sort it. The server publishes the message in the /output topic.

## Sample results
![screen1](https://user-images.githubusercontent.com/19910970/177228502-f105e6ff-0152-4fca-a9c9-899d8c7ed179.png)
![screen2](https://user-images.githubusercontent.com/19910970/177228513-404c10a2-50a4-4cb1-b427-db995badef97.png)
![screen3](https://user-images.githubusercontent.com/19910970/177228522-f65ec53c-e4f0-4ee7-b264-c02c5f8ca939.png)
