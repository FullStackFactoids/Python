with open('myfile.txt', 'w') as f:
    f.write("Hello, World!") # Here, f is automatically closed when it's no longer needed.

#Fun Facts
with open('newfile.txt', 'w') as f:
    f.write("This is a new file!") # Here, f is automatically closed when it's no longer needed.