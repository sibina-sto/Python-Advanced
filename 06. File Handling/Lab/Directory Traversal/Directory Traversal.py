import os

directory_files = os.listdir()
directory_dect = {directory_file.split(".")[1]:[] for directory_file in directory_files}
for files in directory_files:
    file_name, extension = files.split(".")[0], files.split(".")[1]
    directory_dect[extension].append(file_name)
with open("C:\\Users\\vigyr\Desktop\\reports.txt","w") as file:
    for key in sorted(directory_dect):
        file.write(f".{key}\n")
        for value in directory_dect[key]:
            file.write(f"- - - {value}.{key}\n")
