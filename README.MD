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

### Automation Things:

1. Port Scanner – Identify open TCP ports
2. Server Health Check – Monitor CPU, memory & disk
3. Log File Analyzer – Search logs for errors, supports cron & email
4. SMTP Email Sender – Send alerts via smtplib (no extra libs)
5. Automated Backup – Backup folders with timestamps
6. Docker Status Checker – Track container states
7. Kubernetes Pod Checker – Get pod & container status across namespaces

