import os
import string
import shutil

def exRoot(root):
    names = os.listdir(root)
    for name in names:
        process(root, name)

def process(root, name):
    path = os.path.join(root, name)
    if(not os.path.isdir(path)):
        return
    singers = string.split(name, ',', 1)
    if(len(singers)<=1):
        return
    targetDir = os.path.join(root, singers[0])
    if(not os.path.exists(targetDir)):
        os.makedirs(targetDir)
    names = os.listdir(path)
    for fileName in names:
        merge(root, singers[0], name, fileName)
    print 'rmdir ' + path
    os.rmdir(path)

def merge(root, singer, dirName, fileName):
    sourceFile = os.path.join(root, dirName, fileName)
    targetFile = os.path.join(root, singer, fileName)
    if(not os.path.exists(targetFile)):
        print 'move ' + targetFile
        shutil.move(sourceFile, targetFile)
    else:
        print 'delete ' + sourceFile
        os.remove(sourceFile)
