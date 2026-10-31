
FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system and Python development dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    locales \
    curl \
    gnupg \
    build-essential \
    cmake \
    git \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-argcomplete \
    python3-flake8 \
    python3-pytest \
    && locale-gen en_US.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Add ROS 2 package repository
RUN curl -fsSL \
    https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
    | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
    > /etc/apt/sources.list.d/ros2.list

# Install the headless ROS 2 Jazzy base and development tools.
RUN apt-get update && apt-get install -y \
    ros-jazzy-ros-base \
    ros-jazzy-demo-nodes-cpp \
    ros-jazzy-demo-nodes-py \
    ros-dev-tools \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init

# Make ROS available in every interactive Bash terminal.
RUN echo 'source /opt/ros/jazzy/setup.bash' >> /etc/bash.bashrc
