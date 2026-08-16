"""Run the Pico driver with state-only and MoveIt planning RViz views."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def _include(package, launch_file, launch_arguments=None):
    return IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare(package), "launch", launch_file])
        ),
        launch_arguments=(launch_arguments or {}).items(),
    )


def generate_launch_description():
    serial_port = LaunchConfiguration("serial_port")
    baudrate = LaunchConfiguration("baudrate")
    auto_connect = LaunchConfiguration("auto_connect")
    debug_position_commands = LaunchConfiguration("debug_position_commands")

    return LaunchDescription(
        [
            DeclareLaunchArgument("serial_port", default_value="/dev/ttyACM0"),
            DeclareLaunchArgument("baudrate", default_value="115200"),
            DeclareLaunchArgument("auto_connect", default_value="true"),
            DeclareLaunchArgument("debug_position_commands", default_value="false"),
            _include(
                "pico_6dof_robot_driver",
                "driver.launch.py",
                {
                    "serial_port": serial_port,
                    "baudrate": baudrate,
                    "auto_connect": auto_connect,
                    # Keep the driver's state-only RViz alongside MoveIt RViz.
                    "launch_rviz": "true",
                    "debug_position_commands": debug_position_commands,
                },
            ),
            # driver.launch.py already starts robot_state_publisher using the
            # same description URDF, so do not create a duplicate here.
            _include("ros2_6dof_robot_moveit_config", "move_group.launch.py"),
            _include("ros2_6dof_robot_moveit_config", "moveit_rviz.launch.py"),
        ]
    )
