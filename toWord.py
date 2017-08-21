import os
import string
import shutil


class Counter:
    index = 0


theLetters = string.ascii_lowercase
mergeLetters = {'b':'q', 'd':'p', 'n':'u'}
mergeWords = dict()
sortedKeys = []
topLimit = 3000
lengthLimit = 3 + 1
rootPath = '../../Downloads/sentence/'
counter = Counter


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
                    sortedKeys.append(list(key))
                values.append(item)
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
    key_chars = sortedKeys
    while key_chars.__len__() > 100:
        first_index = from_index(copy_list(letters), key_chars)
        key_chars = key_chars[first_index:]


def from_index(letters, key_chars):
    result_chars = []
    first_index = 0
    not_matched = True
    for chars in key_chars:
        if not_matched:
            first_index += 1
        if letters.__len__() < lengthLimit:
            break
        if contain_all(letters, chars):
            not_matched = False
            result_chars.append(chars)
            remove_all(letters, chars)
    if letters.__len__() < 7:
        counter.index += 1
        print(str(counter.index) + "-" + str(key_chars.__len__()) + " -- " + ','.join(letters))
        print(','.join(str_chars(result_chars)))
    return first_index


def str_chars(charss):
    result = []
    for chars in charss:
        result.append('|'.join(mergeWords[''.join(chars)]))
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
