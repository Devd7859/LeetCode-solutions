class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        i = len(s) - 1
        
        # Step 1: Skip all trailing spaces from the end
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # Step 2: Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length
    
#Alternate Solution
'''class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])
'''