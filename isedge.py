import numpy as np 


# function to determine of a certain pixel lies on the edge of a black-white shape

array = np.array([[True, False, True, False, True, True], [True, True, True, True, True, True]])
print(array)

True_counter = np.count_nonzero(array == False)

print(True_counter)