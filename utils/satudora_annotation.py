import os
import sys
import pathlib


def class_process(root_path):
    root_path = pathlib.Path(root_path)
    for class_path in root_path.iterdir():
        annotation = []
        for cam_path in class_path.iterdir():
            cam_dir = pathlib.Path(cam_path)
            for time_dir in cam_dir.iterdir():
                if not os.path.isdir(time_dir):
                    return
                img_path = pathlib.Path(time_dir, "images")
                for img in img_path.iterdir():
                    annotation.append(str(img))
        if class_path.stem == "shelf":
            label = 0
        elif class_path.stem == "others":
            label = 1
        else:
            print("error")

        with open(pathlib.Path(root_path, "label")) as f:
            for i in annotation:
                f.write("\n".join("{} {}".format(i, label)))


if __name__=="__main__":
    root_path = sys.argv[1]
    class_process(root_path)
