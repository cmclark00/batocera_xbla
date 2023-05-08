import os

# Get the user's home directory
home_dir = os.path.expanduser("~")

# Get the path to the XBLA_Unpacked folder
xbla_unpacked_dir = os.path.join(home_dir, "XBLA_Unpacked")

# Define a function to create a text file named after each file in the XBLA_Unpacked folder, with the extension .xbox360, and inside that .xbox360 text file list the original file name without the extension.
def create_xbox360_text_file(file_name):
    # Create a text file with the same name as the file, with the extension .xbox360
    with open(os.path.join(xbla_unpacked_dir, file_name + ".xbox360"), "w") as f:
        # Write the original file name without the extension to the text file
        f.write(file_name)


# Iterate over all of the files in the XBLA_Unpacked folder
for file in os.listdir(xbla_unpacked_dir):
    # If the file is not a directory
    if not os.path.isdir(os.path.join(xbla_unpacked_dir, file)):
        # Create a text file for the file
        create_xbox360_text_file(file)

# Print a message to let the user know that the operation was successful
print("Conversion Complete!")