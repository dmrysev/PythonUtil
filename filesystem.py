import os
import re
import subprocess
from pathlib import Path
from shutil import copy

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def write_to_file(content, filepath):
    with open(filepath, 'w') as f:
        f.write(content)        

def copy_file_to_dir(sourceFilepath, destinationDirpath):
    filename = os.path.split(sourceFilepath)[1]
    destinationFilepath = os.path.join(destinationDirpath, filename)
    copy(sourceFilepath, destinationFilepath)
    return destinationFilepath

def get_file_name(filepath):
    filename = os.path.basename(filepath)
    filename = os.path.splitext(filename)[0]
    return filename

def get_dir_path(filepath):
    dirPath = os.path.split(filepath)[0]
    return dirPath
    
def find_files_recursively(dir_path: str, file_name_pattern: str):
    for path in Path(dir_path).rglob(file_name_pattern):
        yield path
