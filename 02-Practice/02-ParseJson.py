from collections import defaultdict


def errorLine(logfile):
    errorCount = 0
    with open(logfile,'r') as file:
        for line in file:
            if "error" in line.lower():
                print(f"ERROR Line {line.strip()}")
                errorCount = errorCount + 1
    return errorCount

filenamwe = 'Syslog.log'
result = errorLine(filenamwe)
print(result)


# Counting each Log Type 
levels = defaultdict(int)
with open('Syslog.log','r') as file:
    for line in file:
        for level in ['DEBUG','ERROR','DEBUG','WARNING']:
            if level in line.upper():
                levels[level] = levels[level] + 1
print(dict(levels))
