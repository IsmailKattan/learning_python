import os 
os.chdir(os.path.expanduser("~/Desktop"))
file = open(r"Python\txt1.txt","a")
file.write("\r\nElzero Web School => 1")
myRange = range(0,50)
for num in myRange :
    file.write("\r\nAppended => Elzero Web School")

file.close()