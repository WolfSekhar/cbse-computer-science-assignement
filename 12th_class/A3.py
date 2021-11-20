# Remove all the lines that contain the character `a' in a file and write it to another file.

file = open("file.txt","w+")
newfile = open("file_with_only_a.txt","w+")
for line in file:
    if("a" in line):
        newfile.write(line)
file.close()
newfile.close()
