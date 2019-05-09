#!/bin/bash

python3 main.py --root_path ./data --video_path ucf_jpg --annotation_path ucfTrainTestlist/ucf101_01.json \
	--result_path results --dataset ucf101 --n_classes 400 --n_finetune_classes 101 \
	--pretrain_path models/resnet-34-kinetics.pth --ft_begin_index 4 \
	--model resnet --model_depth 34 --resnet_shortcut A --batch_size 128 --n_threads 4 --checkpoint 5
