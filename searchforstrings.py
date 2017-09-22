import os
import time

print("This script will take a folder of .txt files and search them for strings stored in a .txt file, with each string on its own line.")

#get path to store results under
print('')
print("This script will store the results for each book in an individual file.")
print("What path should the file be created under?")
print("**Note: if the path includes the folder this script is under, you can start at that level. Otherwise you need to start at the top.")
resultspath = str(input(": "))

#file path for dir with the files with book text to search through
print("")
bookspath = str(input("Folder path: "))

#file path for file with the strings to find
print("")
sourcepath = str(input("Source .txt path: "))

#start timer
starttime = time.gmtime()

#array for storing search results
results = []

#get strings to find in books
f = open(sourcepath, 'r')
#f.readlines() returns an array of all the lines in the text file f
stringstofind = f.readlines()
f.close()

#get books
booktextfiles = []
#os.walk returns an array something along the lines of [dir path, names of dirs in dir, names of files in dir]
for (dirpath,dirnames,filenames) in os.walk(bookspath):
    #add the filenames to datafiles
    booktextfiles.extend(filenames)
    
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
    
#for storing performance data
perdata = []
    
booknum = 0
#for each book...
while booknum < len(booktextfiles):
    #start book timer
    booktimer = time.gmtime()
    
    #get text of book
    f = open(bookspath+"\\"+booktextfiles[booknum], mode='r', encoding='utf8')
    booklines = f.readlines()
    f.close()
    
    #create/open a file for storing results from this book
    results = open(resultspath+"\\"+booktextfiles[booknum]+"results.txt","w")
    
    linenum = 0
    #for each line in book...
    while linenum < len(booklines):
        #create element to temporarily store book's element for this line's data
        result = []
        
        #for each string to find...
        for string in stringstofind:
            #find string i in string of line linenum
            locations = findString(booklines[linenum],i)

            #if any occurances were actually found...
            if len(locations) > 0:
                #add them to the results list
                result.append([string[0:len(string)-1],locations])
                
            #to help avoid crashing? IDK if this actually helps or not
            time.sleep(0.01)
            
        #if any results, add them to the file
        if len(rslt) > 0:
            results.write(result)
        
        #next line in book
        linenum = linenum + 1        
    
    #close results file
    results.close()
    
    #next book
    booknum = booknum +1
    
    #end book timer
    perdata.append([])
    perdata[booknum]['filepath'] = bookspath+"\\"+booktextfiles[booknum]
    perdata[booknum]['bookanalysisstart'] = booktimer
    perdata[booknum]['totalbooktime'] = time.gmtime()-booktimer
    perdata[booknum]['linesinbook'] = linenum
    #perdata[booknum]['
    results.write("")
    results.write(perdata[booknum])

print(results)
