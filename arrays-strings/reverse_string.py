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