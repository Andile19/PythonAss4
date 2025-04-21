#Quesition 1
def read_and_write_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, "r") as infile:
            content = infile.read()

        # Modify the content (e.g., converting it to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"File content has been modified and written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
read_and_write_file("input.txt", "output.txt")
