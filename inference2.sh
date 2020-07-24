#!/bin/bash

# allow remote X connections
# http://wiki.ros.org/docker/Tutorials/GUI

docker build -t inference -f Dockerfile.inference .

xhost +

docker run -itd \
    --user=root \
    --env="DISPLAY" \
    --volume="/etc/group:/etc/group:ro" \
    --volume="/etc/passwd:/etc/passwd:ro" \
    --volume="/etc/shadow:/etc/shadow:ro" \
    --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --runtime=nvidia \
    --privileged --name inference \
    --network car\
    --env=QT_X11_NO_MITSHM=1 inference bash



