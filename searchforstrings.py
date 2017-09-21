import os

print("This script will take a folder of .txt files and search them for strings stored in a .txt file, with each string on its own line.")

print("")
datapath = str(input("Folder path: "))

print("")
sourcepath = str(input("Source .txt path: "))

f = open(sourcepath, r)
sourcestrings = f.readlines()
f.close()

datafiles = []
for (dirpath,dirnames,filenames) in os.walk(datapath):
    datafiles.extend(filenames)
    
dcounter = 0
while dcounter < len(dcounter):
    f = open(datafiles[i],r)
    data = f.readlines()
    
    tcounter = 0
    while tcounter < len(data):
        
        for i in data[tcounter]:
            str.find(
    
    dcounter = dcounter +1
