# MoveIt configuration for the rough 6-DOF arm

Build and source the workspace before launching:

```bash
cd ~/ros2_ws
colcon build --packages-up-to ros2_6dof_robot_moveit_config
source install/setup.bash
```

Test planning and execution with the mock hardware:

```bash
ros2 launch ros2_6dof_robot_moveit_config demo.launch.py
```

Control the physical robot through the Pico driver:

```bash
ros2 launch ros2_6dof_robot_moveit_config real_robot.launch.py \
  serial_port:=/dev/ttyACM0
```

The real-hardware launch starts the driver, control UI, robot state publisher,
`move_group`, a state-only RViz window, and the MoveIt MotionPlanning RViz
window. It deliberately does not start the mock `ros2_control` controller
manager. In the MotionPlanning window, use the `manipulator` planning group,
plan first, verify the trajectory, and then execute it. Start with the robot
clear of obstacles and be ready to stop it.

Useful launch arguments are `serial_port`, `baudrate`, `auto_connect`, and
`debug_position_commands`.
