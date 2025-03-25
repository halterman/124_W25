# f is a file object
f = open('mary.txt')
# Read each line as text
for line in f:
    # Remove trailing newline character
    print(line.strip())
f.close() # Close the file
