# # Option 1
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # Iterate over the array, keep a temporal vector
#         # to store visited chars, and break when needed
#         visited = set()
#         i = 0  # iterator
#         tmp_n = 0

#         # vars to store best result
#         max_n = 0
#         while i < len(s):
#             if s[i] in visited:
#                 if tmp_n > max_n:
#                     max_n = tmp_n
#                 i = i - tmp_n + 1
#                 tmp_n = 0
#                 visited = set()
#             else:
#                 tmp_n += 1
#                 visited.add(s[i])
#                 i += 1
#         if tmp_n > max_n:
#             return tmp_n
        
#         return max_n

    
# Option 2
class Solution:  # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Iterate over the array, keep a temporal vector
        # to store visited chars, and break when needed
        visited = []

        # vars to store best result
        max_n = 0
        for char in s:
            if char in visited:
                max_n = max(len(visited), max_n)
                # Here' s the trick. Do not start from the beginning
                aux = visited.index(char)
                visited = visited[aux+1:]
            visited.append(char)
        
        return max(len(visited), max_n)

