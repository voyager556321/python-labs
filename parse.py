import os

# Specify the directory containing the .txt files
directory = 'student_marks'

# List all files in the specified directory
files = os.listdir(directory)

# Filter for .txt files
txt_files = [file for file in files if file.endswith('.txt')]

# Loop through each .txt file and open it for reading
for txt_file in txt_files:
    file_path = os.path.join(directory, txt_file)  # Get the full path to the file
    with open(file_path, 'r') as file:  # Open the file for reading
        # Read the content
        content = file.readlines()  # Read all lines in the file
        # Parse the data (example: print each line)
        for line in content:
            print(line.strip())  # Print each line without extra spaces

