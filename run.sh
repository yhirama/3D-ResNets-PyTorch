#!/bin/bash

python3 main.py --root_path /mnt/hdd3tb/action_recog \
--video_path img --annotation_path label/metadata.json \
--result_path satudora_34_5f_pre_result --dataset satudora \
 --n_classes 400 --n_finetune_classes 2 --ft_begin_index 4 --model resnet\
 --model_depth 34 --resnet_shortcut A --batch_size 128 --n_threads 4 --checkpoint 5
