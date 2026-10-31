# ROS 2 Learning

This repository is a ROS 2 Jazzy development workspace intended to run in an
Ubuntu 24.04 GitHub Codespace. The devcontainer installs the headless ROS 2
Jazzy base, colcon, rosdep, and the development tools; no ROS installation on
the Windows host is required.

## Open in Codespaces

Create or reopen the Codespace using `.devcontainer/devcontainer.json`. The
post-create step resolves package dependencies and builds `ros2_ws`. New Bash
terminals source `/opt/ros/jazzy/setup.bash` automatically.

## Build

From the repository root in the Codespace:

```bash
cd ros2_ws
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths src --ignore-src --skip-keys=ament_python -r -y
colcon build
source install/setup.bash
```

After rebuilding, source `ros2_ws/install/setup.bash` in each terminal where
you want to run the workspace package. The base ROS environment is sourced
automatically; the workspace overlay is not.

## Run the publisher and subscriber

Open two terminals in the Codespace. In the first, run:

```bash
cd /workspaces/ROS2_Learning/ros2_ws
source install/setup.bash
ros2 run my_robot_controller talker
```

In the second terminal, run:

```bash
cd /workspaces/ROS2_Learning/ros2_ws
source install/setup.bash
ros2 run my_robot_controller listener
```

The publisher sends `std_msgs/msg/String` messages on the `chatter` topic once
per second, and the subscriber prints each message it receives. Stop either
node with Ctrl+C.
