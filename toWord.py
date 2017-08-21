import os
import string
import shutil

theLetters = string.ascii_lowercase
mergeLetters = {'b':'q', 'd':'p', 'n':'u'}
mergeWords = dict()
topLimit = 5000
lengthLimit = 3 + 1
rootPath = '../../Downloads/sentence/'


def merge_words():
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
    # print(mergeWords)
    with open(rootPath + 'topLimit.txt', 'w') as limitFile:
        for key, values in mergeWords.items():
            limitFile.write(key + ':' + str(values) + '\n')


def merge_letter(word):
    for key, value in mergeLetters.items():
        word = word.replace(value, key)
    return word


def main():
    merge_words()
    letters = list(merge_letter(theLetters))
    key_chars = []
    for key in mergeWords.keys():
        key_chars.append(list(key))
    result_chars = []
    for chars in key_chars:
        if letters.__len__() < lengthLimit:
            break
        if contain_all(letters, chars):
            result_chars.append(chars)
            remove_all(letters, chars)
    print(str(letters))
    print(str_chars(result_chars))


def str_chars(charss):
    result = []
    for chars in charss:
        result.append(mergeWords[''.join(chars)])
    return result


def contain_all(letters, chars):
    check_all = copy_list(letters)
    for char in chars:
        if not check_all.__contains__(char):
            return False
        else:
            check_all.remove(char)
    return True


def copy_list(lst):
    result = []
    for item in lst:
        result.append(item)
    return result


def remove_all(letters, chars):
    for char in chars:
        letters.remove(char)


main()
