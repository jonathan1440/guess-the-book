import os

print("This script will take a folder of .txt files and search them for strings stored in a .txt file, with each string on its own line.")

#file path for dir with the files with book text to search through
print("")
datapath = str(input("Folder path: "))

#file path for file with the strings to find
print("")
sourcepath = str(input("Source .txt path: "))

#array for storing search results
results = []

#get strings to find in books
f = open(sourcepath, r)
#f.readlines() returns an array of all the lines in the text file f
stringstofind = f.readlines()
f.close()

#get books
datafiles = []
#os.walk returns an array something along the lines of [dir path, names of dirs in dir, names of files in dir]
for (dirpath,dirnames,filenames) in os.walk(datapath):
    #add the filenames to datafiles
    datafiles.extend(filenames)
    
#This function exists solely so I could use recursion :)
#Also to return multiple indices if possible, instead of the one returned by .find(
def findString (strtosearch,strtofind):
    #store indices of occurances
    num = []

    def fs (strtosearch,strtofind,startIndex):
        #look for first occurance, store index as ind
        ind = strtosearch.find(strtofind,startIndex)

        #if occurance occured,
        if ind != -1:
            #store index outside
            num.append(ind)
            #find next index with adjusted start index
            fs(strtosearch,strtofind,ind+1)

    #find all occurances
    fs(strtosearch,strtofind,0)

    #return indices of occurances    
    return num
    
dcounter = 0
#for each book...
while dcounter < len(datafiles):
    #get text of book
    f = open(datafiles[i],r)
    booklines = f.readlines()
    f.close()

    #create element for this book's data
    results.append([])
    
    tcounter = 0
    #for each line in book...
    while tcounter < len(booklines):
        #create element in book's element for this line's data
        results[dcounter].append([])
        
        #for each string to find...
        for i in stringstofind:
            #find string i in string booklines[tcounter]
            locations = findString(booklines[tcounter],i)

            #if any occurances were actually found...
            if len(locations) != 0:
                #add them to the results list
                results[dcounter][tcounter].append([i,locations])
            
        #next line in book
        tcounter = tcounter + 1
    
    #next book
    dcounter = dcounter +1


print(results)
