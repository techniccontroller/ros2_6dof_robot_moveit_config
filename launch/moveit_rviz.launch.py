from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_moveit_rviz_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("rough_6dof_arm", package_name="ros2_6dof_robot_moveit_config").to_moveit_configs()
    return generate_moveit_rviz_launch(moveit_config)
