import os 
import subprocess
os.chdir(os.path.expanduser("~/Desktop"))
print(os.getcwd())
os.mkdir("Python")
file = open("Python/assign.py","a")

fileList = ["import os\r\n",
"os.chdir(os.path.expanduser(\"~/Desktop\"))\r\n",
"myRange = range(1,51)\r\n",
"for num in myRange :\r\n",
"    if num == 25 :\r\n",
"        indexedFile = open(\"Python/special-text.txt\",\"x\")\r\n",
"        indexedFile.close()\r\n",
"        continue\r\n",
"    indexedFile = open(f\"Python/txt{num}.txt\",\"w\")\r\n",
"    indexedFile.write(\"Elzero Web School => {%d}\" % num)\r\n",
"    indexedFile.close()\r\n",
"\r\n",
"\r\n",
"print(os.getcwd())\r\n",
"print(os.path.dirname(os.path.abspath(__file__)))\r\n",
"print(__file__)\r\n",
"file_count = 0\r\n",
"for file_name in os.listdir(\"Python\"):\r\n",
"    file_path = os.path.join(\"Python\", file_name)\r\n",
"    if os.path.isfile(file_path):\r\n",
"        file_count += 1\r\n",
"print(f\"{file_count}\")\r\n"
]
file.writelines(fileList)
file.close()
print(os.getcwd())
subprocess.run(["python","Python/assign.py"])