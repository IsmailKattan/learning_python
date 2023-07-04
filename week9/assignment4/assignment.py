import os 
os.chdir(os.path.expanduser("~/Desktop"))
file_count = 0

for file_name in os.listdir("Python"):
    file_path = os.path.join("Python", file_name)
    if os.path.isfile(file_path):
        file_count += 1
        
myRange = range(0,file_count)
willBeDeleted = range(file_count-10,file_count)

for file in myRange :
    if file in willBeDeleted :
        os.remove(rf"Python\txt{file}.txt")