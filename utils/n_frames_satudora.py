from __future__ import division, print_function

import os
import sys
import pathlib
import subprocess


def class_process(root_path):
    root_path = pathlib.Path(root_path)
    for class_path in root_path.iterdir():
	for cam_path in class_path.iterdir():
	    cam_dir = pathlib.Path(cam_path)
            for time_dir in cam_dir.iterdir():
                if not os.path.isdir(time_dir):
                    return
                img_path = pathlib.Path(time_dir, "images")

                for file_name in img_path.iterdir():
                    image_indices = []
                    if 'jpg' not in file_name:
                        continue
                    image_indices.append(file_name)

                if len(image_indices) == 0:
                    print('no image files', file_name)
                    n_frames = 0
                else:
                    image_indices.sort(reverse=True)
                    n_frames = len(image_indices)
                    print(time_dir, n_frames)
                with open(str(pathlib.Path(img_path, 'n_frames')), 'w') as dst_file:
                    dst_file.write(str(n_frames))


if __name__=="__main__":
  root_path = sys.argv[1]
  class_process(root_path)
