###############################################################################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        i = 0
        size = len(nums)

        # 1. Iterate over elements
        while i < size:
            if a == i:
                i += 1
                continue

            if nums[a] != nums[i]:
                a = i
                i += 1
                continue

            del nums[i]
            size = len(nums)

        return len(nums)

