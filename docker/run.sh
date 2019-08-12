#!/bin/sh

#$1: gpu number
IMAGE="3dresnet"

sudo nvidia-docker build ./docker/ -t $IMAGE
sudo NV_GPU=$1 nvidia-docker run \
    -v $(pwd):/3D-ResNets-PyTorch \
    -v /mnt/hdd3tb/action_recog:/mnt/hdd3tb/action_recog \
    --rm \
    --shm-size=16G \
    -it $IMAGE \
    /bin/bash

