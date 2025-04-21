#Quesition 2 
def file_error_handling():
    filename = input("Please enter the filename: ")

    try:
        # Open the user-provided file in read mode
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function
file_error_handling()
