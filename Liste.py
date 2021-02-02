import numpy as np

test1 = np.array([1,2])
test2 = np.array([4,5])
test3 = np.array([6,7])

array = np.array([test1[0], test2[0], test3[0]])
print(array)

distance_list = [4, 2, 5, 1, 9, 0]

best_polygon_position = distance_list.index(min(distance_list))
print(best_polygon_position)


#with open(r"C:\\Users\\victo\\nlp1\\Cities.txt", encoding="utf-8") as f:
#    cities = f.read().splitlines()

#print(cities)


