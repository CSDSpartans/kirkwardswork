name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open("tuesdayafternoon.txt", 'r')    #open file for reading

line = file_input.readline()
print (line, end = '')
line = file_input.readline()
print (line, end = '')
line = file_input.readline()
print (line, end = '')
line = file_input.readline()

line_counter = 1 
stanza_counter = 1
total_number_of_lines_in_file = 3

while line != '':                      # while not end of file
    if line == '\n':
      stanza_counter += 1 
      print(" ") 
    else:
      if line_counter < 10:
        
        print(line_counter,") ",line, end = '')              # don't print another new line
        line_counter += 1
      else:
        print(line_counter,")",line, end = '')              # don't print another new line
        line_counter += 1
    line = file_input.readline()
    total_number_of_lines_in_file += 1



print(" ")
print(" ") 
print("The number of lines in the poem is:",line_counter - 1)
print("The number of stanzas in the poem is:", stanza_counter)



print("The total number of lines in the file is:", total_number_of_lines_in_file)
file_input.close() 

print("The song \"Tuesday Afternoon\" first appeared on the album \033[3mDays of Future Passed\033[0m in 1967.")
print("The members of the band are Graeme Edge, Justin Hayward, John Lodge, Ray Thomas, Mike Pinder.")
