from launch import LaunchDescription
from launch_ros.actions import Node
import ament_index_python.packages

import os

def generate_launch_description():

  default_params_yaml = os.path.join(
    ament_index_python.packages.get_package_share_directory('hri_safety_sense'),
    'cfg', 'params.yaml')

  return LaunchDescription([
    Node(
      package="hri_safety_sense",
      executable="hri_joystick_node",
      name="hri_joystick_node",
      parameters=[default_params_yaml],
    ),
  ])
