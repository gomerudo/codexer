# class Solution:
#     def reverseWords(self, s: str) -> str:
#         i = len(s) - 1
        
#         words = []
#         start = None
#         end = None
#         while i >= 0:
#             if s[i] == " ":
#                 if end is not None:
#                     start = i + 1
#                     words.append(s[start:end])
#                     start = None
#                     end = None
#             if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9'):
#                 if end is None:
#                     end = i + 1  # Because index is exclusive
#             i -= 1
        
#         if end is not None:
#             words.append(s[0:end])

#         return ' '.join(words)


class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        
        pattern = "[a-zA-Z\d]+"
        # pattern = "blue"
        res = re.findall(pattern, s)
        print(res)
        if res:
            return ' '.join(res[::-1])
        
        return []