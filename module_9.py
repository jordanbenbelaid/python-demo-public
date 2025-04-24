#reading our file
sample_file = open("textfile.txt", "r")

for line in sample_file:
    print(line)
    
sample_file.close()

print("==================================================================")
#writing to a file
sample_file_write = open("textfile.txt", "w")

sample_file_write.write("This is the second line of the file \nThis is the third line of the file")

sample_file_write.close()


#re-reading the file
sample_file_two = open("textfile.txt", "r")

for line in sample_file_two:
    print(line)

sample_file_two.close()

print("==================================================================")


#appending a file
sample_file_append = open("textfile.txt", "a")

sample_file_append.write("\nI have added this to the end of the file")

sample_file_append.close()


#re-read one more time
sample_file_three = open("textfile.txt", "r")

for line in sample_file_three:
    print(line)

sample_file_three.close()