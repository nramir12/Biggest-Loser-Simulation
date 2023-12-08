# permutations using library function
from itertools import permutations
import numpy as np


# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3, 4, 5, 6], 4)
listPerm = list(perm)
print(listPerm)
calnum = '3'
secnum = '2'
x = 1
y = 1
z = 1

for i in listPerm:
    line1 = ""
    for j in i:
        line1 += str(j)
    ltline1 = list(line1)
    sample_array = np.array(ltline1).reshape(2, 2)
    print(sample_array)

    if (sample_array[0][0] == '4') or (sample_array[0][0] == '5') or (sample_array[0][0] == '6'):
        print("Loteria Card")
    elif (sample_array[1][0] == '4') or (sample_array[1][0] == '5') or (sample_array[1][0] == '6'):
        print("Loteria Card")
    elif (sample_array[0][1] == '1') or (sample_array[0][1] == '2') or (sample_array[0][1] == '3'):
        print("Loteria Card")
    elif (sample_array[1][1] == '1') or (sample_array[1][1] == '2') or (sample_array[1][1] == '3'):
        print("Loteria Card")
    else:
        print(x, "Bingo Card------------>")
        x += 1
    print('_______________')
