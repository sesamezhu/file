import os
import string
import shutil

mergeLetters = {'b':'q', 'd':'p', 'n':'u'}
# mergeWords = dict()
topLimit = 3000
lengthLimit = 3 + 1
rootPath = '../../Downloads/sentence/'


def main():
    # names = os.listdir(root)
    index = 0
    with open(rootPath + '10000.txt') as wordFile:
        with open(rootPath + 'topLimit.txt', 'w') as limitFile:
            for item in wordFile:
                index += 1
                if index > topLimit:
                    break
                if item.__len__() < lengthLimit:
                    continue
                limitFile.write(item)
                print(str(index) + ":" + item.rstrip())
                print(item.__len__())
                # key = fields[1]
                # mergeValue = mergeWords[key]
                # if(mergeWords[key] == None) :
                #     mergeWords.update(key, )


main()
