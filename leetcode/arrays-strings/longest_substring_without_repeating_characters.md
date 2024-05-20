# Problem

Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**

>**Input:** `s = "abcabcbb"`<br>**Output:** `3`<br>**Explanation:** The answer is `"abc"`, with the length of 3.

**Example 2:**

>**Input:** s = "bbbbb"<br>**Output:** 1<br>**Explanation:** The answer is "b", with the length of 1.

**Example 3:**

>**Input:** s = "pwwkew"<br>**Output:** 3<br>**Explanation:** The answer is `"wke"`, with the length of 3.<br>Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.
 

**Constraints:**

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.

# Solution

## Intuition

The idea is to iterate over the array and keep a memory of visited chars. If no
repeated char is found, the max length is the length of the memory. If we find
a repeated char, we must restart immediately after the repeated character. This
last observation is key:

- If at every restart we moved one position only, we would be always founding the repeated chars. E.g., in `ubacawxyz` we would traverse `uabca`, `baca`, `aca` unnecesarelly.
- It's smarter to restart after the first position of the repeated character. In the example above we would then skip 3 unnecessary steps and instead try `ubaca` and then `cawxyz`

## Approach
<!-- Describe your approach to solving the problem. -->

## Complexity
- Time complexity: `O(n)`
- Space complexity: `O(n)`

## Code
```python
# Option 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Iterate over the array, keep a temporal vector
        # to store visited chars, and break when needed
        visited = set()
        i = 0  # iterator
        tmp_n = 0

        # vars to store best result
        max_n = 0
        while i < len(s):
            if s[i] in visited:
                if tmp_n > max_n:
                    max_n = tmp_n
                i = i - tmp_n + 1
                tmp_n = 0
                visited = set()
            else:
                tmp_n += 1
                visited.add(s[i])
                i += 1
        if tmp_n > max_n:
            return tmp_n
        
        return max_n

    
# Option 2
class Solution:  # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Store visited chars and the max length found so far
        visited = []
        max_n = 0

        # Iterate over the array
        for char in s:
            
            # If we end up revisiting a character:
            if char in visited:
                # 1. Mark our traversal as finished
                max_n = max(len(visited), max_n)

                # Here' s the trick. Do not start from the beginning but from
                # the position after the first occurence of the duplicated char
                aux = visited.index(char)

                # Discard everything up to the first occurrence of the char
                visited = visited[aux+1:]

            # Always add the current char
            visited.append(char)

        # Finally, return the max length        
        return max(len(visited), max_n)

```