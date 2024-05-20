# Problem

Given two binary strings `a` and `b`, return their sum as a binary string.

**Example 1:**

>**Input:** `a = "11"`, `b = "1"`<br>**Output:** "100"

**Example 2:**

>**Input:** `a = "1010"`, `b = "1011"`<br>**Output:** "10101"

**Constraints:**

- `1 <= a.length, b.length <= 104`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

# Solution

## Intuition

The problem suggests (not clearly specified) that we are constrained to work
with strings. Thus, we need a function that handles the four cases of simple
binary sum: `0 + 0`; `0 + 1`; `1 + 0`; `1 + 1`. Once such function exists, we
can simply iterate over the strings and sum digit by digit.

## Approach

Key considerations:
- The maximum sum of two one-digit binaries is `10`, which is the result of `1 + 1`.
- The maximum sum of three one-digit binaries is `11`, which is the result of `1 + 1 + 1`.

1. Write a function that sums 1-digit binaries. This implies 4 cases: 
   1. `0 + 0` -> `0`
   2. `0 + 1` -> `1`
   3. `1 + 0` -> `1`
   4. `1 + 1` -> `10` (Note this implies carrying a `1`).
2. Write a function that sums two binary numbers, assuming first argument is the one with the longest length. The key steps are:
   1. Pad the shortest binary with 0s at the right. This allows for easy manipulation.
   2. We will perform a sum of three one-digit binaries: `residual/carriage + digit of array1 + digit of array2`. Set `carriage1 = 0` and iterate arrays in reverse order (that's how we sum):
      1. Sum `carriage1` and `digit of array1`. This yields a `1-digit sum` and a new `carriage2`.
      2. Sum the `1-digit sum` and the `digit of array2`. This is the resulting sum of this iteration.
      3. Append the sum of step 2 to the resulting string (concatenate to the right).
      4. Since we performed the sum of three one-digit binaries, "worst" case is to have a carry of `1`. Make `carriage1 = 1` if this was the case.
   3. Return result.
      1. If there was no residual after step 2, return the concatenated string.
      2. If there was a residual, concatenate it to the right and return.

## Complexity
- Time complexity: `O(max(a.length, b.length))`
- Space complexity: `O(max(a.length, b.length) + 1)`

## Code
```python
class Solution:
    
    def oneDigitBinarySum(self, cx, cy):
        if cx == "0" and cy == "0":
            return "0", "0"
        if cx == "0" and cy == "1":
            return "1", "0"
        if cx == "1" and cy == "0":
            return "1", "0"
        if cx == "1" and cy == "1":
            return "0", "1"

    # TODO: improve to use less memory. We don't really need padding.

    def binarySum(self, x, y):
        # Pad shortest to make them the same lenght
        diff = len(x) - len(y)
        y = '0'*diff + y  
        
        res = ""
        car1 = "0"

        # Iterating in reverse order
        for cx, cy in zip(x[::-1], y[::-1]):
            # 1. Add carriage and digit from array1
            sumres, car1 = self.oneDigitBinarySum(cx, car1)
            # 2. Add resulting sum and digit from arrray2
            sumres, car2 = self.oneDigitBinarySum(sumres, cy)

            # 3. Concatenate result to the right
            res = sumres + res

            # 4. Override carriage1 if car2 is 1, which means
            if car2 == "1":
                car1 = car2

        # If there was no residual, 
        if car1 == "0":
            return res

        return car1 + res

    def addBinary(self, a: str, b: str) -> str:
        if len(a) >= len(b):
            return self.binarySum(a, b)

        return self.binarySum(b, a)

```
