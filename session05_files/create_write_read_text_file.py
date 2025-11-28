#python script to demonstarte how to create,  write and read from a text file

# import the os module

import os    #module to enable our script work with the operating system(Os) and its file system

# create a file to craete and write to a file

def create_file(path, content):
    """
    create a file with the given path and writes the specified content to it

    :param path: path of the file to be created
    param content: content of the file to be created
    """
    with open(path, "w", encoding='utf-8') as f:
        f.write(content)
        print(f"file created and contents written succesfully")

# get and display  the current working directory
current_dir = os.getcwd()
print(f"current_directory is {current_dir}")


# get and display the path to the files directory by going up one folder
file_directory = os.path.abspath(os.path.join(current_dir,'..', "files"))
print(f"file_directory is {file_directory}")

# specify and display the file path and name of the  file to be created
file_path = os.path.join(file_directory, "hello.txt")

# specify the text/content to be written to the file using a hard-coded/user-input string
# content =input("please🙏 enter the text to write to the file: ")

content = "Hello 👋 from text files in python"

# call
create_file(file_path, content)

# todo write the code  to read the contents of the hello.txt file and display them
# Read and display the contents of hello.txt
def read_from_file(path):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="UTF-8") as f:
                content = f.read()
                print(f"Content are  from {path}")
                print(content)
        except Exception as e:
            print(f"the error  is from  {path}:\n{e}")

