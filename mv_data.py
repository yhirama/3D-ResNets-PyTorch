import os
import sys
import pathlib

from PIL import Image


def read_anno(root_path):
    root_path = pathlib.Path(root_path)
    for cam_dir in root_path.iterdir():
        for time_dir in cam_dir.iterdir():
            anno_path = pathlib.Path(time_dir, "action_annotation")
            if not os.path.exists(str(anno_path)):
                continue
            for anno_file_path in anno_path.iterdir():
                with open(anno_file_path, "r") as f:
                    label = int(f.read())
                file_name = anno_file_path.stem
                img = Image.open(str(pathlib.Path(root_path,
                                                  cam_dir.stem,
                                                  time_dir.stem,
                                                  "images",
                                                  file_name + ".jpg")))
                if label == 0:
                    output_path = str(pathlib.Path(
                        "/mnt/hdd3tb/action_recog/shelf",
                        cam_dir.stem,
                        time_dir.stem,
                        "images"
                    ))
                elif label == 1:
                    output_path = str(pathlib.Path(
                        "/mnt/hdd3tb/action_recog/others",
                        cam_dir.stem,
                        time_dir.stem,
                        "images"
                    ))
                else:
                    print("error")

                os.makedirs(output_path, exist_ok=True)
                print(output_path)
                img.save(str(pathlib.Path(output_path,
                                          file_name + ".jpg")))


if __name__ == '__main__':
    args = sys.argv
    # Select output dir of processed yolo
    data_path = args[1]
    read_anno(data_path)
