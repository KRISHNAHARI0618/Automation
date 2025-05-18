import subprocess
import os
from sys import stdout

folderName = "Hari-Own"
os.makedirs(folderName,exist_ok=True)

for i in range(1,5):
    fileName = f"Application-{i}.yaml"
    folderToCreate = os.path.join(folderName,fileName)

    with open(folderToCreate,'w') as f:
        f.write(f"Adding This in File Name {folderName}-{i}\n")

subprocess.run(['echo','Hello Hari Vardhan Reddy'])

# Pipe Method

process = subprocess.Popen(['ls'],stderr=subprocess.PIPE,stdout=subprocess.PIPE)

stderr ,stdout = process.communicate()
print(stdout.decode())
print(stderr)

print(os.getcwd())

print(os.listdir())
files = os.listdir()
filesCount = len(os.listdir())
print(filesCount)
for i in range(filesCount):
    if files[i].endswith('.yaml'):
        print(f"This is File {files[i]}")

# SubProcess Call() Method

exit_code = subprocess.call(['mkdir', 'DataOps'])
# If already exists gives error tell the another  method

# Subprocess.run() method

result = subprocess.run(['ls'],capture_output=True,text=True)
print(result)

subprocess.run(['git','status'])


