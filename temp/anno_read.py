from scipy import io

train_list = [str(i)+'_'+str(j) for i in range(1, 21) for j in range(1, 4)]
val_list = [str(i)+'_'+str(j) for i in range(21, 27) for j in range(1, 4)]
test_list = [str(i)+'_'+str(j) for i in range(27, 41) for j in range(1, 4)]

matdata = io.loadmat('../data/Labels_MERL_Shopping_dataset/4_3_label.mat', squeeze_me=True)

print(matdata['tlabs'])

"""
0    Reach To Shelf (reach to shelf)

1    Retract From Shelf (retract hand from shelf)

2    Hand In Shelf (extended period with hand in the shelf)

3    Inspect Product (inspect product while holding it in hand)

4    Inspect Shelf (look at shelf while not touching and not reaching for the shelf)
"""
assert len(matdata['tlabs']) == 5, 'error'
for i in range(5):
    data = matdata['tlabs'][i]
    assert len(data) > 0, 'error'
    for j in data:
        print(j)

