#!/usr/local/bin/python

import sys
import re
import os

def getBigramCounts(textData):
  """ Function to clean and format the text data """
  bigramCounts = {}

  for line in textData:
    line = re.sub(r'[^\w\s]','',line)
    words = line.split()
    print words
    fileID = words.pop(0)
    
    #words.insert(0,'#')
    #words.append('#')
    for index in range(len(words)-1):
      c_tokens = words[index]
      n_tokens = words[index+1]
      bigram = c_tokens + n_tokens
      print 'The bigram is'
      print bigram
      if bigram in bigramCounts:
        bigramCounts[bigram] = bigramCounts[bigram] + 1
      else:
        bigramCounts[bigram] = 1
    print '\n'
  return bigramCounts

def calculateMatrix(bigramCounts,wordTokens,featureWords):
  counts = []
  CONTEXTS= []
  for word in wordTokens:
    
    print ' Bigrams are '
    print bigramCounts
    temp = []
    contexts = []
    wordType = word.strip()
    for context in featureWords:
      contextWord = context.strip()
      print 'The word is '
      print word.split('\n')[0]
      print 'The context word is '
      print contextWord
      lString = contextWord + wordType
      contexts.append(lString)
      print 'lString is '
      print lString
      if lString in bigramCounts:
        lCount = bigramCounts[lString]
      else:
        lCount = 0
      print 'lCount is '
      print lCount
      temp.append(lCount)
      rString = wordType + context
      print 'rString is'
      print rString
      contexts.append(rString)
      if rString in bigramCounts:
        rCount = bigramCounts[rString]
      else:
        rCount = 0 
      print 'rCount is '
      print rCount     
      temp.append(rCount)
    print '\n\n\n'
    contexts = map(str,contexts)
    temp = map(str,temp)
    counts.append(' '.join(temp))
    CONTEXTS.append(''.join(contexts))
  print CONTEXTS
  return counts

def printToFile(outF,counts):
  fp_write = open(outF,'w')
  for vector in counts:
    fp_write.write(vector)
    fp_write.write('\n')
  fp_write.close()

def readFile(fileName):
  """ Function to read files """
  fp_read = open(fileName,'r')
  data = fp_read.readlines()
  fp_read.close()

  return data

def main():
  """ Main Function """
  if len(sys.argv) != 5:
    print 'Usage : python file.py <txt.done.data (in)> <word tokens file (in)> <feature words file (in)> <co-occurrence matrix file (out)>'
    print 'This code generates the co-occurrence matrix and prints it to a file'
    sys.exit(1)

  taggedF = sys.argv[1]
  wordTokensF = sys.argv[2]
  featureWordsF = sys.argv[3]
  outF = sys.argv[4]

  text = readFile(taggedF)
  wordTokens = readFile(wordTokensF)
  featureWords = readFile(featureWordsF)

  bigramCounts = getBigramCounts(text)
  countsMatrix = calculateMatrix(bigramCounts,wordTokens,featureWords)
  print countsMatrix
  printToFile(outF,countsMatrix)

if __name__ == '__main__':
  main()
