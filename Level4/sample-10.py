print(__name__)
# If the Python interpreter is running this module (the source file)
# as the main program, it sets the special __name__ variable to have a value "__main__".
# If this file is being imported from another module, __name__ will be set to the module's name.

# FUN FACTS

if __name__ == "__main__":
    print("The script is running on its own")
else:
    print("The script is being imported somewhere else")