# 'with' creates a context for the file
# When the block ends, the file will close automatically
with open('new_file.txt') as file:

    for line in file:
        print(line.strip())

# content = file.read(10)
# print(content)

# content = file.read(5)
# print(content)