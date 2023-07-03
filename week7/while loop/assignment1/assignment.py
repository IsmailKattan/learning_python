num = -1
counter = 0
while num <= 0:
    num = int(input("Please enter a Number for loop ").capitalize().strip())
    if num <= 0 :
        print(f"Number {num} Is Not Larger Than 0 ")
while num>1:
    if(num-1 == 6) :
        num-=1
        continue
    print(num-1)
    counter+=1
    num-=1

if num > 0 :
    print(f"{counter} Numbers Printed Successfully.")