
# Program that asks for a filename and handles errors

def read_file():
    filename = input("Enter the filename to read: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile content:")
            print(content)
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
        
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
# Create a sample file for testing
with open("sample.txt", "w") as f:
    f.write("This is a sample file for testing error handling.")

# Call the function (try with "sample.txt" or an invalid filename)
read_file()