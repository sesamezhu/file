import os
import string
import shutil

mergeLetters = {'b':'q', 'd':'p', 'n':'u'}
mergeWords = dict()
topLimit = 5000
lengthLimit = 3 + 1
rootPath = '../../Downloads/sentence/'


def merge_words():
    # names = os.listdir(root)
    index = 0
    with open(rootPath + '10000.txt') as wordFile:
            for item in wordFile:
                index += 1
                if index > topLimit:
                    break
                if item.__len__() < lengthLimit:
                    continue
                item = item.rstrip()
                key = merge_letter(item)
                values = mergeWords.get(key)
                if values is None:
                    values = []
                    mergeWords[key] = values
                values.append(item)
    print(mergeWords)
    with open(rootPath + 'topLimit.txt', 'w') as limitFile:
        for key, values in mergeWords.items():
            limitFile.write(key + ':' + str(values) + '\n')


def merge_letter(word):
    for key, value in mergeLetters.items():
        word = word.replace(value, key)
    return word


merge_words()
