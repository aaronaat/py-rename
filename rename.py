import os
import sys

def rename(path, name, start, stop):
    
    #split the file name at .
    name = name.split('.')

    #put the user's start/stop parameters into reversed list
    span = list(reversed(range(start, stop + 1)))

    #sort the contents of path in reverse order
    folder = sorted(os.listdir(path), reverse=True)

    #list only the files with correct prefix and file extension
    files = [x for x in folder if (x.startswith(name[0]) and x.endswith(name[1]))]

    #iterate through list of files and update name from span
    for i, filename in enumerate(files):
        destination = name[0] + str(span[i]) + '.' + name[1]
        os.rename((path + filename), (path + destination))

rename(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
