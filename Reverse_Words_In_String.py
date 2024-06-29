#https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        l = s.split(" ")#create list of by splitting on basis of space
        l = l[::-1]#reverse list
        result = ""
        for st in l:
            if st != '':
                result += ' ' + st #add space before each non empty string
        return result[1:] #return the result and slice the first space
    

class Solution(object):
    def reverseWords(self, s):
        l = s.split(" ")
        l = l[::-1]
        result = " ".join([x for x in l if x != ''])#same code using shortcut suntax
        return result
        """
        :type s: str
        :rtype: str
        """
        

class Solution(object):
    def reverseWords(self, s):
        return " ".join([x for x in s.split(" ")[::-1] if x != '']) #more shortcut added
        """
        :type s: str
        :rtype: str
        """
#optimized  
class Solution(object):
    def reverseWords(self, s):
        s = s.strip() #remove white spaced
        l = s.split() #split on the basis of white space (by default)
        l = l[::-1] #reverse
        result = " ".join(l)#join all words and add space in them
        return result
        """
        :type s: str
        :rtype: str
        """
#same optimized solution but with shortcut
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
        