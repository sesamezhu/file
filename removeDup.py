import os
import re

def processRoot(root):
    regular = re.compile('(.*)(?=\(\d+\))')
    names = os.listdir(root)
    for name in names:
        process(os.path.join(root,name), regular)

def process(path, regular):
    if(not os.path.isdir(path)):
        return
    names = os.listdir(path)
    errors = []
    for name in names:
        fname, fext = os.path.splitext(name)
        if fext != '.mp3':
            continue
        match = regular.match(fname)
        if match:
            checkDup(path, match.group(1) + fext, name)

def checkDup(path, name, dupName):
    full = os.path.join(path, name)
    fullDup = os.path.join(path, dupName)
    if(os.path.exists(full)):
        stat = os.stat(full)
        statDup = os.stat(fullDup)
        if(stat.st_size < statDup.st_size):
            print 'replace ' + dupName
            os.remove(full)
            os.rename(fullDup, full)
        else:
            print 'remove ' + dupName
            os.remove(fullDup)
    else:
        print 'rename ' + dupName
        os.rename(fullDup, full)
