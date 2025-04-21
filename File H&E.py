# Program that asks for a filename and handles errors

def create_sample_file():
    """Creates a sample file for testing purposes."""
    with open("sample.txt", "w") as f:
        f.write("This is a sample file for testing error handling.")

def read_file():
    """Prompts the user for a filename and handles errors."""
    while True:
        filename = input("Enter the filename to read (or type 'exit' to quit): ")
        
        if filename.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        try:
            # Attempt to open and read the file
            with open(filename, "r") as file:
                content = file.read()
                print("\nFile content:")
                print(content)
                break  # Exit the loop after successful reading
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
            
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Please try again.")
            
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please try again.")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Create a sample file for testing
create_sample_file ='sample.txt'

# Call the function (try with "sample.txt" or an invalid filename)
read_file()