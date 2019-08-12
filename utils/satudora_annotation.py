import os
import sys
import pathlib
import numpy as np

train_list = ["30", "32", "34", "36", "38", "40"]
test_list = ["42", "46", "48"]

def class_process(root_path):
    root_path = pathlib.Path(root_path)
    train = []
    test = []
    for class_path in root_path.iterdir():
        print(class_path)
        if class_path.stem == "label":
            continue
        for cam_path in class_path.iterdir():
            cam_dir = pathlib.Path(cam_path)
            for time_dir in cam_dir.iterdir():
                if not os.path.isdir(time_dir):
                    return
                img_path = pathlib.Path(time_dir, "images")
                print(img_path)
                for img in img_path.iterdir():
                    if cam_path.stem in train_list:
                        train.append(str(img))
                    elif cam_path.stem in test_list:
                        test.append(str(img))

    np.random.seed(0)
    np.random.shuffle(train)
    np.random.seed(0)
    np.random.shuffle(test)
    with open(pathlib.Path(root_path, "../label", "train.txt"), "w") as f:
        for i in train:
            if "shelf" in i:
                label = 0
            elif "others" in i:
                label = 1
            else:
                print("error")
            f.write("{} {}".format(i, label))
            f.write("\n")
    with open(pathlib.Path(root_path, "../label", "test.txt"), "w") as f:
        for i in test:
            if "shelf" in i:
                label = 0
            elif "others" in i:
                label = 1
            else:
                print("error")
            f.write("{} {}".format(i, label))
            f.write("\n")


if __name__=="__main__":
    root_path = sys.argv[1]
    class_process(root_path)
