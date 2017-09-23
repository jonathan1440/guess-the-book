import time

print("This script will take a folder of .txt files and search them for strings stored in a .txt file, with each string on its own line.")

#get path to store results under
print('')
print("This script will store the results for each book in an individual file.")
print("What path should the file be created under?")
print("**Note: if the path includes the folder this script is under, you can start at that folder's level. Otherwise you need to start at the top.")
resultspath = str(input(": "))
 
#file path for dir with the files with book text to search through
print("")
bookspath = str(input("Path to folder with text of books to search: "))

#file path for file with the strings to find
print("")
sourcepath = str(input("Path to file with strings to search for: "))

#start timer
starttime = time.gmtime()

#get strings to find in books
f = open(sourcepath, 'r')
#f.readlines() returns a list of all the lines in the text file f
stringstofind = f.readlines()
#always .close() a file after you are done using it
f.close()

#get books
booktextfiles = []
#os.walk returns a list something along the lines of [dir path, names of dirs in dir, names of files in dir]
for (dirpath,dirnames,filenames) in os.walk(bookspath):
    #add the filenames of the files with the book texts to datafiles
    booktextfiles.extend(filenames)
#----<----
    
#This function exists solely so I could use recursion :)
#Also to return multiple indices if possible, instead of just one returned by .find()
def findString (strtosearch,strtofind):
    #store indices of occurances
    indices = []

    def fs (strtosearch,strtofind,startIndex):
        #look for first occurance, store index as ind
        ind = strtosearch.find(strtofind,startIndex)

        #if occurance occured,
        if ind != -1:
            #store index outside function
            indices.append(ind)
            #find next index adjusted to start after the index of the previous occurance
            fs(strtosearch,strtofind,ind+1)
        #----<----
    #----<----

    #implement fs() to find all occurances
    fs(strtosearch,strtofind,0)

    #return indices of occurances    
    return indices
#----<----
    
#for storing performance data, will be a dict
perdata = []
    
#counters
booknum = 0
counter = 0
#for each book...
while booknum < len(booktextfiles):
    #start book timer
    booktimer = time.gmtime()
    
    #get text of book
    f = open(bookspath+"\\"+booktextfiles[booknum], mode='r', encoding='utf8')
    booklines = f.readlines()
    f.close()
    
    #create or open a file for storing results from this book
    results = open(resultspath+"\\"+booktextfiles[booknum]+"results.txt","w")
    #if it already existed, empty it
    results.truncate()
    
    #counter
    linenum = 0
    #for each line in book text file...
    while linenum < len(booklines):
        #create list to temporarily store book's element for this line's data
        result = []
        
        #for each string to search for...
        for string in stringstofind:
            #find string "string" in string of line "linenum"
            locations = findString(booklines[linenum],string)
            #for debug
            print(counter)
            counter += 1
            
            #if any occurances were found...
            if len(locations) > 0:
                #add them to the results list
                result.append([string[0:len(string)-1],locations])
            #----<----
                
            #to help avoid crashing? IDK if this actually helps or not
            #time.sleep(0.00005)
        #----<----
            
        #if any results, add them to the results file
        if len(result) > 0:
            results.write(str(linenum))
            
            #for each string to search for...
            for i in range(len(result)):
                #create empty variable to store everythign I want on one line in the results file
                #unfortunately the .write() function only takes strings, so...
                writeline = ""
                #add the particular string to line
                writeline.join(str(result[i][0]))
                #using str.join() is more efficient than += when compiling
                writeline.join(": ")
                
                #for each index in the line where the string occured...
                for j in range(len(result[i][1])):
                    #add the index to the line
                    writeline.join(str(result[i][1][j]))
                    writeline.join(", ")
                #----<----
                
                #write the line to the results file
                results.write(writeline)
            #----<----
        #----<----
        
        #next line in book
        linenum += 1 
    #----<----
    
    #close results file
    results.close()
    
    #next book
    booknum += 1
    
    #end book timer
    perdata.append([])
    perdata[booknum]['filepath'] = bookspath+"\\"+booktextfiles[booknum]
    perdata[booknum]['bookanalysisstart'] = booktimer
    perdata[booknum]['totalbooktime'] = time.gmtime()-booktimer
    perdata[booknum]['linesinbook'] = linenum
    #perdata[booknum]['

    #record performance data
    results.write("")
    for name,data in perdata.items():
        results.write(name+" : "+str(data))
    #----<----
#----<----



