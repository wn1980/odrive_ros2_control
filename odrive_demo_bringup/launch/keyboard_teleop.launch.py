from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name='keyboard_teleop_node',
            output='screen',
            prefix = 'xterm -T keyboard_teleop -e',
            remappings=[
                ('cmd_vel', '/diffbot_base_controller/cmd_vel_unstamped')
            ]
        ),
    ])
