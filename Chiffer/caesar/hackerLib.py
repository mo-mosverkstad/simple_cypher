#!/usr/bin/env python

def genEnglishDic():
	return[word.rstrip() for word in open('english.dic')]

def checkEnglish(wordList, dic):
	num_total = len(wordList)
	num_match = 0
	for word in wordList:
		if word in dic: num_match = num_match + 1
		#else: print word
	return num_match * 1.0000 / num_total * 100

def isEnglish(msg):
	return checkEnglish(msg.split(' '), genEnglishDic())

