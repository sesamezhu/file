import os
import string
import shutil

def main(root):
    names = os.listdir(root)
    with open(root + '.txt', 'w') as mergedTxt:
        for name in names:
            process(root, name, mergedTxt)

def process(root, name, mergedTxt):
    fname, fext = os.path.splitext(name)
    if(fext != '.txt'):
        print name + ' is not text'
        return
    path = os.path.join(root, name)
    mergedTxt.write('\n\n')
    mergedTxt.write('-------')
    mergedTxt.write(name)
    mergedTxt.write('-------')
    mergedTxt.write('\n')
    with open(path) as text:
        mergedTxt.write(text.read())
    print name

