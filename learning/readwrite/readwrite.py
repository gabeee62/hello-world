# You can use python to read and write files.
# Files can be opened in read, write, or append mode with 'r', 'w', or 'a' as the second argument respectively.
f = open("funny.txt", 'w')
# Initializes variable f as the text file "funny.txt" in write mode.
# If the file is in the same directory as the program you can use the relative path, else you must use the absolute
# path, seen here.
# --------------------------------------------------
# You can write data to a file if it has been opened in write mode with .write().
f.write('I love python!')
# --------------------------------------------------
# It's good practice to close the file once you are done using it with .close().
f.close()
# --------------------------------------------------
# Append mode is used to add data to a file without overwriting the current data.
f = open("funny.txt", 'a')
# Opening "funny.txt" in append mode
f.write('\nI love Java!')
f.close()
# This writes "I love Java!" on a new line in the file, without overwriting the original text.
# --------------------------------------------------
# Read mode allows the computer to read all of the data in the selected file.
r = open("readme.txt", 'r')
print(r.read())
r.close()
# This would print all of the contents of the "readme.txt" file.
# We can change this to have the computer read line by line by using the "for" command.
r = open("readme.txt", 'r')
w = open("writeme.txt", 'w')
for line in r:
    line = line.removesuffix('\n')
    w.write(line + ' ' + str(len(line)) + '\n')
w.close()
r.close()
# This code reads line by line each title in the "readme.txt" file, then writes each title and its character count
# onto the new file "writeme.txt".
# Because each line in a text file ends with a new line indicator (\n), we have to first remove it, then add it back
# to the final string so everything looks just right.
# Don't forget to close all of your files once you're done using them!
# --------------------------------------------------
# You can also use the "with" statement to open a file and close it immediately after you're finished using it,
# so you don't have to worry about closing it!
with open("funny.txt", 'r') as f:
    print(f.read())
# You can then check *if* the file is closed with the .closed flag:
print(f.closed)
# The program outputs True because the "funny.txt" file has been closed.

