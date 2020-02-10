import os
import re
import subprocess
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


def listValueOrDefault(list, index, default = None):
    return list[index] if len(list) > index else default


def checkFileExistance(filepath):
    if not os.path.exists(filepath):
        msg = 'File not found: %s' % filepath
        raise IOError(msg)


def saveToFile(content, filepath):
    with open(filepath, 'w') as f:
        f.write(content)


def execute(command):
    p = subprocess.Popen(
        command, universal_newlines=True, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()

    if p.returncode != 0:
        errorMsg = '%s %s' % (output, error)
        e = subprocess.CalledProcessError(p.returncode, command)
        e.message += errorMsg
        raise e

    return output


def copyToDir(sourceFilepath, destinationDirpath):
    filename = os.path.split(sourceFilepath)[1]
    destinationFilepath = os.path.join(destinationDirpath, filename)
    copy(sourceFilepath, destinationFilepath)

    return destinationFilepath


def splitStringBySpacesRespectQuotes(string):
    values = [t.strip('"') for t in re.findall(r'[^\s"]+|"[^"]*"', string)]

    return values


def getFileName(filepath):
    filename = os.path.basename(filepath)
    filename = os.path.splitext(filename)[0]

    return filename


def getDirPath(filepath):
    dirPath = os.path.split(filepath)[0]

    return dirPath