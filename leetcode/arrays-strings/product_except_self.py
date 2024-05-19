class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        i = 0
        
        product = 1
        zeros = 0
        while i < len(nums):
            if nums[i] == 0:
                zeros += 1
            else:
                product *= nums[i]
            i += 1


        if zeros >= 2:
            return answer

        i = 0
        while i < len(nums):
            if zeros and nums[i] == 0:
                answer[i] = product
            if not zeros:
                answer[i] = product // nums[i]
            i += 1
        return answer