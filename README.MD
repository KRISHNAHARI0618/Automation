## Python Automation Notes:

### Day 01

1. Python Env Set Up and activate venv
2. File Handling `Read and Write`

### Writing the content to file
```
with open('DevOps.txt','w') as file:
    file.write("I am Learning DevOps Course Since 2023 \n")
    file.write("I am Even Learning DSA Course \n")
```
### Reading The file 
```
with open('DevOps.txt','r') as file:
    for line in file:
        print(line)
```

### File openings
1. r -> read
2. w -> write
3. a -> append
4. x -> create and write(error if exists)
5. b -> binary mode
6. + -> read and write

