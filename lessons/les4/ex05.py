list1 = [x for x in range(1, 20)]
print(list1)

list1 = list(map(lambda x: x + 10, list1))
print(list1)