my_range = range(1,21)
for num in my_range:
    if num == 6 or num == 8 or num == 12 :
        continue
    if num < 10 :
        print(f"0{num}") 
    else : 
        print(num)
print("All Numbers Printed")