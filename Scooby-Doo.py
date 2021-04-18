##Define Character names to variables.
Characters = ("Shaggy\nScooby-Doo\nDaphne\nVelma")
Characters2 = ("\nFred\nScrappy")
##Call of creation and naming or new file to write to.
fh = open('Scooby.txt', 'w')
##Write original file with select character names
fh.write(Characters)
##Close file
fh.close
##Open file and add second list of charaters via additional variable
fh = open('Scooby.txt', 'a')
fh.write(Characters2)
#Close file
fh.close