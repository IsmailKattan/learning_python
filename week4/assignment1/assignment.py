my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
unique_list.pop(-1)
print(unique_list)
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4