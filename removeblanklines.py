print("This script will remove blank lines from a .txt file")
path = str(input("What is the path for the .txt file you would like to edit? "))

f = open(path,mode='r',encoding='utf8')
lines = f.readlines()
f.close()

nonblank = []

c = 0
while c < len(lines):
    if len(lines[c]) > 3:
        nonblank.append(lines[c])

    c += 1

f = open(path,'w')
f.truncate()

for i in nonblank:
    f.write(i)

f.close()
