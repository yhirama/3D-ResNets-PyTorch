import numpy

from scipy import io

"""
0    Reach To Shelf (reach to shelf)

1    Retract From Shelf (retract hand from shelf)

2    Hand In Shelf (extended period with hand in the shelf)

3    Inspect Product (inspect product while holding it in hand)

4    Inspect Shelf (look at shelf while not touching and not reaching for the shelf)
"""
label_list = ['Reach-To-Shelf', 'Retract-From-Shelf', 'Hand-In-Shelf', 'Inspect-Product', 'Inspect-Shelf']
def read_path(num):
    path = []
    matdata = io.loadmat('../data/Labels_MERL_Shopping_dataset/{}_label.mat'.
                         format(num), squeeze_me=True)
    assert len(matdata['tlabs']) == 5, 'error'

    for i in range(5):
        data = matdata['tlabs'][i]
        if len(data) == 0:
            continue
        # assert len(data) > 0, 'error data {}'.format(matdata['tlabs'])
        if type(data[0]) is numpy.uint16:
            data = [data]
            print(data)
        for j in data:
            for k in range(j[0], j[1]):
                path.append('{}/{}_crop/image_{}.jpg {}'.format(label_list[i], num,
                                                                 str(k).zfill(5),
                                                                 i+1))
                print(str(k).zfill(5))

    return path


if __name__=='__main__':
    train_list = [str(i)+'_'+str(j) for i in range(1, 21) for j in range(1, 4)]
    val_list = [str(i)+'_'+str(j) for i in range(21, 27) for j in range(1, 4)]
    test_list = [str(i)+'_'+str(j) for i in range(27, 31) for j in range(1, 4)]

    path = []
    for i in train_list:
        path.extend(read_path(i))
    path = '\n'.join(path)
    with open('../data/merl_label/train_list.txt', 'w') as f:
        f.writelines(path)
 
    path = []
    for i in val_list:
        path.extend(read_path(i))
    path = '\n'.join(path)
    with open('../data/merl_label/val_list.txt', 'w') as f:
        f.writelines(path)
 
    path = []
    for i in test_list:
        path.extend(read_path(i))
    path = '\n'.join(path)
    with open('../data/merl_label/test_list.txt', 'w') as f:
        f.writelines(path)
