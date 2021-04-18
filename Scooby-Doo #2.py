##Open previously created file
f = open('Scooby.txt', 'r')
##Read file
info = f.read()
##Print contents of file
print(info)
#Close file
f.close()
print("\n")
##Create variable for contents inside txt file
charfile = open('Scooby.txt')
##Choose to only read specific lines
readline =[0,1,2]
##Print out specific names from list and eliminate whitespace
for position, line in enumerate(charfile):
    if position in readline:
        line = line.strip('\n')
        print(line)