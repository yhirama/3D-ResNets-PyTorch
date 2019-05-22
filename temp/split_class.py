import os
import shutil

"""
0    Reach To Shelf (reach to shelf)

1    Retract From Shelf (retract hand from shelf)

2    Hand In Shelf (extended period with hand in the shelf)

3    Inspect Product (inspect product while holding it in hand)

4    Inspect Shelf (look at shelf while not touching and not reaching for the shelf)
"""


with open('../data/merl_label/train.txt', 'r') as f:
    for m in f.readlines():
        path, label = m.split()
        path = path.split('/')
        des_path = '../data/merl_jpg/{}/{}'.format(label, path[2])
        root_path = '../data/merl_jpg/{}'.format(path)
        os.makedirs(des_path, exist_ok=True)

        proc = shutil.move(root_path, des_path)
        print(proc)
