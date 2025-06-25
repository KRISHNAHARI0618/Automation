import argparse
from ast import parse 
import cmd
import os
import shutil


parser = argparse.ArgumentParser()
parser.add_argument("number1",help="Please Number1")
parser.add_argument("number2",help="please Number2")
parser.add_argument("operation",help="Please enter operation")

args = parser.parse_args()

print(args.number1)
print(args.number2)
print(args.operation)

n1 = int(args.number1)
n2 = int(args.number2)
result = 0
if args.operation == "add":
    result = n1+n2
else:
    print("Quits The application")

print(result)


print(shutil.disk_usage(os.getcwd()))
