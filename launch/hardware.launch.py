from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the ros2_rpi_as5048a encoder.launch.py
        ExecuteProcess(
            cmd=['ros2', 'launch', 'ros2_rpi_as5048a', 'encoder.launch.py'],
            output='screen'
        ),

        # Run mavlink_router_launcher with specified parameters
        ExecuteProcess(
            cmd=[
                'ros2', 'run', 'mavlink_router_launcher', 'mavlink_router_node',
                '--ros-args', '-p', 'endpoint:=192.168.0.189:14550', 
                '-p', 'device:=/dev/ttyACM0', '-p', 'baudrate:=57600'
            ],
            output='screen'
        ),
        
        # Run micro_ros_agent for serial communication
        ExecuteProcess(
            cmd=['ros2', 'run', 'micro_ros_agent', 'micro_ros_agent', 'serial', '--dev', '/dev/ttyAMA1', '-b', '921600'],
            output='screen'
        ),
    ])

