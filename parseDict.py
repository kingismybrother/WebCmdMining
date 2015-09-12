# -*- coding: utf-8 -*-
__author__ = 'AllenCHM'

# def loadText():

# fileName = u'主张词语（中文）.txt'
# fileName = u'flower.txt'
fileName = u'正面情感词语（中文）.txt'
def loadTextDict(fileName):
    f = open(fileName)
    wordsList = []
    for i in f.readlines():
        i = i.strip()
        if i:
            wordsList.append(i)
    f.close()
    return wordsList
