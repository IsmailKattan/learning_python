# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
counter = 1
my_nums.sort(reverse=True)
for num in my_nums :
    if num % 5 == 0 :
        print(f"\"{counter} => {num}\"")
        counter+=1
print("All Numbers Printed")

# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"