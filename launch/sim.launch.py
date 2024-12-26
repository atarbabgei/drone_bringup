from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Execute the PX4 SITL build and run
        ExecuteProcess(
            cmd=['bash', '-c', 'cd ~/Firmware-PX4/passive-rotating-prop/PX4-Autopilot && make px4_sitl gz_x500_passive_rotating_prop'],
            output='screen'
        ),
        # Launch the micro_ros_agent
        ExecuteProcess(
            cmd=['ros2', 'run', 'micro_ros_agent', 'micro_ros_agent', 'udp4', '-p', '8888'],
            output='screen'
        ),
        
        # Launch the ros_gz_bridge for force/torque parameter bridge
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_bridge', 'parameter_bridge', 
                 '/propeller_guard_joint/force_torque@geometry_msgs/msg/Wrench@gz.msgs.Wrench'],
            output='screen'
        ),
        
        # Launch the ros_gz_bridge for joint state parameter bridge
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_bridge', 'parameter_bridge',
                 '/propeller_guard_joint/joint_state@sensor_msgs/msg/JointState@gz.msgs.Model'],
            output='screen'
        ),
        
        # Launch the px4_ros_visualizer
        ExecuteProcess(
            cmd=['ros2', 'launch', 'px4_ros_visualizer', 'px4_visualizer.launch.py'],
            output='screen'
        ),
    ])
