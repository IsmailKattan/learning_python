# Inputs

num1 = int(input("enter num1 ").strip())
num2 = int(input("enter num2 ").strip())
operation = input("enter \"+\" Or \"-\" Or \"*\" Or \"/\" Or \"%\" ").strip()

if operation == '+':
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
elif operation == "%":
    print(num1%num2)
else :
    print(f"ERROR No such operator named {operation}")

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800