# python3

file = str(input("Filepath to file: "))

f = open(file,'r')
data = f.readlines()
f.close()

unique = []

for i in data:
    uniq = True
    for j in unique:
        if i == j:
            uniq = False

    if uniq == True:
        #unique.append(i[0:len(i)-1])
        unique.append(i)

f = open(file,'w')
f.truncate()

for i in unique:
    f.write(i)

f.close()
