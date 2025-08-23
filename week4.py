# Create a new file and write initial content
file = open('newFile.txt', 'w')
content = "Hello, this is file creation content.\nLet's get started."

file.write(content.upper())  # Modify the content (convert to uppercase)

#create a program that reads a file
file = open('newFile.txt', 'r')
data = file.read()
print(data)


try:
    file = open('newFile.pdf', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")