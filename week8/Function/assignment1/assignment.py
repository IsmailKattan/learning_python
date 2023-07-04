def calculate(num1, num2, ope = "A") :
    if (type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float) and type(ope) == str:
        ope = ope.lower()
        if ope[0] == "a" :
            return num1 + num2
        elif ope[0] == "s" :
            return num1 -num2
        elif ope[0] == "m" :
            return num1 * num2 
        else :
            print(f"{ope} doesn't supported")
            return 0
    elif type(ope) != str :
        print(f"operator should be a string")
        return 0
    else :
        print(f"{num1} and {num2} are not integer of float number")
        return 0
    
# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200