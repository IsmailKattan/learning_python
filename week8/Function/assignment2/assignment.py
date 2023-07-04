def addition(*nums) :
    result = 0
    for num in nums:
        if type(num) == int or type(num) == float :
            if num == 10 :
                continue
            if num == 5:
                result -= num
            else :
                result += num
        else :
            print(f"{num} is not integer or float number")
    return result


# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160