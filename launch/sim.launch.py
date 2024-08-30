from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Execute the PX4 SITL build and run
        ExecuteProcess(
            cmd=['bash', '-c', 'cd ~/Firmware-PX4/rolling_drone/PX4-Autopilot && make px4_sitl gz_x500_spinning_guard'],
            output='screen'
        ),

        # Launch the micro_ros_agent
        ExecuteProcess(
            cmd=['ros2', 'run', 'micro_ros_agent', 'micro_ros_agent', 'udp4', '-p', '8888'],
            output='screen'
        ),
        
        # Launch the ros_gz_bridge for parameter_bridge
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_bridge', 'parameter_bridge', '/joint_states@sensor_msgs/msg/JointState@gz.msgs.Model'],
            output='screen'
        ),
        
        # Launch the px4_ros_visualizer
        ExecuteProcess(
            cmd=['ros2', 'launch', 'px4_ros_visualizer', 'px4_visualizer.launch.py'],
            output='screen'
        ),
    ])
