import os

# output_dir = "learn_files"
# os.makedirs(output_dir,exist_ok=True)

# for i in range(1,6):
#     filename = f"file{i}.yaml"
#     filepath = os.path.join(output_dir,filename)

#     with open(filepath,'w') as f:
#         f.write(f"Adding DevOps Strings to Files {i} \n")
#         f.write("devops\n" if i %2 == 0 else "data\n")

# print("Files are created Successfully")


# 1: Add Directory or Path where to create 
# 2: os.makedirs() --> it will create a folders
# 3: filecreation with os.path.join(directoryname,filename)
# 4: open(filename,'w) as f --> opens the files as f 
# 5: Write someting to files as first line --> f.write(f"Any Content")
# 6: add devops if the if the file is even count else add data

# dirName = "DataOps"
# os.makedirs(dirName,exist_ok=True)

# for i in range(1,10):
#     filename = f"Simple{i}.yml"
#     filepath = os.path.join(dirName,filename)

#     with open(filepath,'w') as myFile:
#         myFile.write("Please Check The file is available or not \n this is learning files so please don't worry \n")
#         myFile.write("DevOps at enfd  \n" if i % 2 == 0 else "Development At The End..\n ")
# print("files are created succesfully ")


# with open("devops.yaml",'w') as f:
#     f.write("Adding This to First Line \n ")
#     for i in range(1,10):
#         f.write(f"adding the line number {i} \n ")


# with open("devops.yaml" ,'r') as f:
#     for i in f.readlines():
#         if "4" in i:
#             print(i)
# f.close()

# print(os.getcwd())

# os.chdir("DataOps")

# print(os.getcwd())

# FolderName = "LearnDevOps"
# os.makedirs(FolderName,exist_ok=True)
# os.chdir("LearnDevOps")
# print(os.getcwd())


# for i in range(1,10):
#     fileName = f"Data-{i}.yaml"
#     folderName = os.path.join(FolderName,fileName)

#     with open(FolderName,'w') as f:
#         f.write("Adding Two Lines Of Code ....")

    
#     for i  in os.listdir():
#         print(i)


dirName = "DataOrders"
os.makedirs(dirName,exist_ok=True)

for i in range(1,10):
    fileName = f"Data-{i}.yml"
    folderToAdd = os.path.join(dirName,fileName)
    with open(folderToAdd,'w') as fileName:
        fileName.write(f"Adding Text to File {i} - Simples \n ")
        fileName.write(f"Adding DevOps to {fileName} - Development \n")

os.chdir(dirName)

for i in os.listdir():
    print(i)
print(os.getcwd())


