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

import logging
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


logging.basicConfig(filename='Syslog.log',level=logging.DEBUG)

logging.debug("Adding Debug Logs to the file ..")
logging.error("Logging Error Logs to the pod ....")
logging.critical("Adding Critical Logs To The pod...")
logging.warning("adding warning to pod logs ")
logging.info("adding info to the pod logs..")

# for i in range(100):
#     if i % 2 == 0:
#         logging.info("Adding Info to The logs ...")
#     elif i % 4 == 0:
#         logging.debug("Adding Debug To The logs ....")
#     elif i % 3 == 0:
#         logging.warning("This is warning messge...")
#     elif i % 10 == 0:
#         logging.error("Adding Error to the logs")
#     else:
#         logging.critical("Adding Citical To The logs")

myset = {i for i in range(10)}
print(myset)


list1 = [i for i in range(10)]
print(list1)

dict1= { i : 2* i for i in range(10)}
print(dict1)


try:
    if 10 % 0 == 0:
        print("This is error logs")
except Exception as e:
    print(f"This is an Error {e}")
    logging.error(f"Adding {e} as an error in logs")
else:
    print(f"Printing access isse ")
finally:
    print("This is Logging Finally")