class MyContextManager:
    def __enter__(self):
        print("Entering the block")
        return self

    def __exit__(self, type, value, traceback):
        print("Exiting the block")

with MyContextManager() as x:
    print("Inside the block")
# Output:
# Entering the block
# Inside the block
# Exiting the block

# FUN FACTS

with open('file.txt', 'r') as f:
    contents = f.read()
# This will automatically close the file after the nested block of code