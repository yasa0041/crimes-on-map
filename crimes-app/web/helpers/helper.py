import os

def remove_file(filename):
    os.remove(filename)
    print("Deleted file {}", filename)
