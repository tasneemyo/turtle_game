from launch import LaunchDescription
from launch_ros.actions import Node
from my_robot_control import *
def generate_launch_description():
    ld=LaunchDescription()
    random_node=Node(

        package="my_robot_control",
        executable="random",
    )

    move_node=Node(
        package="my_robot_control",
        executable="move",
    )
    kill_node=Node(
        package="my_robot_control",
        executable="kill"
    )
    ld.add_action(random_node)
    ld.add_action(move_node)
    ld.add_action(kill_node)

    return ld


