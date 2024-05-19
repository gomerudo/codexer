class Solution:
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)
                
        while i < n // 2:
            aux = s[i]
            s[i] = s[n-i-1]
            s[n-i - 1] = aux
            i += 1
            
            
    def reverseSingleWord(self, s, start, end):
        i = 0
        n = end - start
        
        while i < n // 2:
            aux = s[i + start]
            s[i + start] = s[n-i-1 + start]
            s[n-i - 1 + start] = aux
            i += 1
        
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Step 1: Reverse the string
        self.reverseString(s)
    
        # Step 2: Fix the words
        i = 0
        
        start = None
        while i < len(s):
            if s[i] == " ":
                if start is not None:
                    self.reverseSingleWord(s, start, i)
                    start = None
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9'):
                if start is None:
                    start = i 
            i += 1
        
        if start is not None:
            self.reverseSingleWord(s, start, len(s))


