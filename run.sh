#!/bin/bash

python3 main.py --root_path ./data --video_path merl_jpg --annotation_path merl_label/metadata1.json \
	--result_path merl_152_16f_nopre_results --dataset merl --n_classes 400 --n_finetune_classes 5 \
	#--pretrain_path models/resnet-152-kinetics.pth --ft_begin_index 4 \
	--ft_begin_index 4 \
	--model resnet --model_depth 152 --resnet_shortcut B --batch_size 64 --n_threads 4 --checkpoint 5
