#!/usr/local/bin/python

import sys
import re
import os

def generateFreqCounts(inF):
  ''' Generate a dictionary containing words and their frequency counts '''
  wordDictionary = {}

  fpRead = open(inF,'r')
  textData = fpRead.readlines()
  fpRead.close()
  i = 0 
  for line in textData:
    line = re.sub(r'[^\w\s]','',line)
    words = line.split()
    #print words
    fileID = words.pop(0)
    i = i+ 1
    print 'Processing ' + fileID + '.....'
    print i
    for idx in range(len(words)):
      wrd = words[idx]
      if wrd in wordDictionary:
        wordDictionary[wrd] = wordDictionary[wrd] + 1
      else:
        wordDictionary[wrd] = 1

  return wordDictionary

def returnSecondElementTuple(tup):
  ''' Returns the second element of the tuple tup '''
  return tup[1]

def printToFile(wordDictionary,outF):
  ''' Prints the words and their frequency counts to a file
      in descending order of the frequency '''

  wordFreqTuples = wordDictionary.items()

  fpWrite = open(outF,'w')
  
  for word, wordFreq in sorted(wordFreqTuples, key = returnSecondElementTuple, reverse = True):
    string = word + ' ' + str(wordFreq) + '\n'
    fpWrite.write(string)

  fpWrite.close()


def main():
  ''' Main function '''
  if len(sys.argv) != 3:
    print "Usage : python file.py <txt.done.data file (in)> <word frequency file (out)>"
    print """ This code generates the list of unique words and their frequency counts 
from a corpus file. The corpus file is a text file containing the audiobook text corpus """

    sys.exit(1)
  

  inF = sys.argv[1]
  outF = sys.argv[2]

  wordDictionary = generateFreqCounts(inF)
  printToFile(wordDictionary,outF)


if __name__ == '__main__':
  main()
