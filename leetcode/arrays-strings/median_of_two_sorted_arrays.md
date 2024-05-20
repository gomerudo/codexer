# Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 
**Example 1:**
>**Input:** `nums1 = [1,3], nums2 = [2]`<br>**Output:** 2.00000<br>**Explanation:** `merged array = [1,2,3]` and median is 2.

**Example 2:**

> **Input:** `nums1 = [1,2], nums2 = [3,4]`<br>**Output:** 2.50000<br>**Explanation:** `merged array = [1,2,3,4]` and median is `(2 + 3) / 2 = 2.5`.
 

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`

# Solution

## Intuition

If the two arrays are sorted, that means we can build the aggregated sorted array with a simple for-loop that traverses both arrays. Once the final array is built, we can return the median which is `n + m / 2`.

A key note here is that an odd array will have an exact median (see Example 1). An even array will have a two-sided median (see Example 2).

## Approach

The approach of this solution is as follows:

1. First compute the `median_idx`. There are two cases:
   1. For exact median, a floor rounding will return the exact index. E.g., `[1, 2, 3] -> len = 3 -> 3 // 2 = 1` 
   2. For a two-sided median, floor rounding will return the index of the last element to contribute to the median. E.g., `[1, 2, 3, 4] -> len = 4 -> 4 // 2 = 2`.
2. Traverse both arrays to build the merged one. Stop when `len(merged) == median_idx + 1`. All information after this index is irrelevant.
3. Return the median:
   1. If exact median, return last element in `merged`
   2. If two-sided median, return the average of the last two elements in `merged`.

## Complexity
- Time complexity: `O(n/2)`
- Space complexity: `O(n/2)`

## Code
```python
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        total_size = n + m 

        median_idx = total_size // 2

        # TODO: Handle special case of n = m = 0 (? What to return)
        merged = []
        current_size = 0

        to_append = None
        while i < n or j < m:
            # Case 1: Traverse both arrays if possible
            if i < n and j < m:
                if nums1[i] < nums2[j]:
                    to_append = nums1[i]
                    i += 1
                else:
                    to_append = nums2[j]
                    j += 1
            # If array1 still has elements but array2 has been consumed
            elif i < n and j >= m:
                to_append = nums1[i]
                i += 1
            # If array2 still has elements but array1 has been consumed
            elif i >= n and j < m:
                to_append = nums2[j]
                j += 1

            merged.append(to_append)
            current_size += 1

            # Stop when we reached the median index
            if current_size - 1  == median_idx:
                break

        # Return the median according to each case
        # Case 1: exact 
        if total_size % 2 == 1:median
            return merged[-1]

        # Case 2: two-sided median
        return (merged[-1] + merged[-2]) / 2
```
