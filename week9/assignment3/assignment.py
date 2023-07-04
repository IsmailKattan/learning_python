import os 
os.chdir(os.path.expanduser("~/Desktop"))
file = open(r"Python\txt1.txt","r")
lines = 0
Words = 0
chars = 0
ls = 0 

for char in file.read() :
    
    if char == "\n" :
        lines += 0.5
        Words += 0.5
    else :
        chars += 1
    if char == " " : 
        Words += 1
    if char == "l" :
        ls += 1

print(int(lines))
print(int(Words))
print(chars)
print(ls)
file.close()