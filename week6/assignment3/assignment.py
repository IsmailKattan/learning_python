age = int(input("Enter your age ").strip())

if age>10 and age<100 :
    print(f"{age} years")
    print(f"{age * 12} months")
    print(f"{int(age * 365/7)} weeks")
    print(f"{age * 365} days")
    print(f"{age * 365 * 24} hours")
    print(f"{age * 365 * 24 * 60} minutes")
    print(f"{age * 365 * 24 * 60} seconds")
else :
    print("out of the range")