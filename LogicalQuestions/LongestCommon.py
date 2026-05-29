class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Take the first string as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this character against all other strings
            for string in strs[1:]:
                # If the string is shorter or character doesn't match
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
                    
        return strs[0]