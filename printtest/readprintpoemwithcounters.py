#   This reads and prints the whole document.
#           It does not prt a blank line after each line of the file

name_of_mydocument = 'mydocument.txt'                # Name the file
file_input = open(name_of_mydocument, 'r')           # open file for reading

line = file_input.readline()                         # read and print title
print(line)
line = file_input.readline()                         # read and print author
print(line)
line = file_input.readline()                         # read and print blank line
print(line)

line = file_input.readline()                         # read first line of actual poem

line_counter = 0                                     # initialize counters
stanza_counter = 1

while line != '':                                     # while not end of file

    if line == '\n':                                    # is line a blank line - which indicates a new stanza
      stanza_counter += 1                                   # increment stanza counter  
      print ()                                              # print blank line
    else:                                               # line is not a blank line
      line_counter += 1                                    # increment line counter
      print(line_counter, line, end = '')                  # print line counter and line, prevent printing another new line
    line = file_input.readline()                        # read next line in file
    
print ()                                               # print blank line
print ()                         
print ("The number of stanzas is ",  stanza_counter)   # print stanza counter

file_input.close()                                     # close file
