import re

def readTxtFile(filename): #takes in txt file path
   txtFile = open(filename)
   txtContents = txtFile.read()
   txtFile.close()
   return txtContents #returns string of file's contents

def textToList(text, delimiter = '\n', cleanup = False): #takes in string, breaks it into list of strings at specified delimiter
   textList = re.split(delimiter, text)
   if cleanup == True: #OPTIONAL ARGUMENT: if third argument is passed as True, the function will "cleanup" empty list items at the start and end
      if textList[0] == '':
         textList.pop(0)
      if textList[-1] == '':
         textList.pop(-1)
   return textList #returns broken up string, now list

def stringIntersect(string1, string2): #takes in two strings
   result = ""
   for char in string1:
    if char in string2 and not char in result:
        result += char
   return result #returns string of all intersecting characters in order

def minIntInList(list): #takes list of ints and returns the minimum from it
   sorted = list.copy()
   sorted.sort()
   return sorted[0]