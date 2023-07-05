def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

def my_min(iterable):
    if not iterable:
        raise ValueError("my_min() arg is an empty sequence")
    min_value = iterable[0]
    for element in iterable[1:]:
        if element < min_value:
            min_value = element
    return min_value

def my_max(iterable):
    if not iterable:
        raise ValueError("my_max() arg is an empty sequence")
    max_value = iterable[0]
    for element in iterable[1:]:
        if element > max_value:
            max_value = element
    return max_value

# my_all
print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False

# my_any
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False

# my_min
print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
