import pandas as pd
import matplotlib as plt

plt.use("Agg")

import os
import pathlib

result_dic = {}
for i in range(1, 63):
    result_dic[i] = 0

def check(img_path, _class):
    img_list = []
    for i in img_path:
        name = str(i).split("/")[-1].strip(".jpg")
        img_list.append(name)
    img_list = img_list

    for i in img_list:
        date, frame = i.split("_")
        count = 0
        # print("date {} frame {}".format(date, frame))
        for j in range(int(frame), int(frame)+500, 5):
            if date +"_"+ str(j).zfill(4) not in img_list: 
                result_dic[count] = result_dic[count] + 1
                break
            count += 1
    return result_dic



def hist(path):
    root_path = pathlib.Path(path)
    n = 0
    for class_path in root_path.iterdir():
        hist_dic = {}
        for cam_path in class_path.iterdir():
            n = 0
            for time_dir in cam_path.iterdir():
                img_path = pathlib.Path(time_dir, "images")
                n += len(list(pathlib.Path(img_path).glob("*.jpg")))
                check(list(pathlib.Path(img_path).glob("*.jpg")), class_path.stem)
                # hist_dic[]
            print(class_path.stem, cam_path.stem, n)
            hist_dic[cam_path.stem] = n
        print(hist_dic)
        with open("./{}_hist.txt".format(class_path.stem), "w") as f:
            for k, v in sorted(hist_dic.items()):
                f.write("{} {} {} \n".format(class_path.stem, k, v)) 





if __name__=="__main__":
    path = "/mnt/hdd3tb/action_recog/img"
    hist(path)
