with open('DevOps.txt','w') as file:
    file.write("I am Learning DevOps Course Since 2023 \n")
    file.write("I am Even Learning DSA Course \n")

with open('DevOps.txt','a') as file:
    file.write("Appending the new line ...\n")

with open('DevOps.txt','r') as file:
    for line in file:
        print(line)


with open('Syslog.log') as log:
    for line in log:
        if 'error' in line:
            print(line.strip())

import os

for i,filename in enumerate(os.listdir('photos')):
    print(i,filename)
    os.rename(f'photos/{filename}',f'photos/image_{i}.txt')

print(os.listdir('photos'))

import json

data = {
    'name' : 'Hari',
    'role' : 'DevOps'
}

with open('data.json','w') as f:
    json.dump(data,f)

with open('data.json','r') as file:
    loaded = json.load(file)
    print(loaded)
    print(loaded['name'])
