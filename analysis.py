import pandas as pd
import matplotlib as plt

plt.use("Agg")

import os
import pathlib


def hist(path):
    hist_dic = {}
    root_path = pathlib.Path(path)
    n = 0
    for class_path in root_path.iterdir():
        for cam_path in class_path.iterdir():
            n = 0
            for time_dir in cam_path.iterdir():
                if not os.path.isdir(time_dir):
                    return
                n += time_dir.glob("*.jpg")
                # hist_dic[]
            print(class_path.stem, cam_path.stem, n)





if __name__=="__main__":
    path = "/mnt/hdd3tb/action_recog/img"
    hist(path)
