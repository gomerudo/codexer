# # Solution 1 
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         countsd1 = {}
#         for n in nums1:  # O (2n + m) for the two arrays
#             if n in countsd1:
#                 countsd1[n] += 1
#             else:
#                 countsd1[n] = 1
                
#         countsd2 = {}
#         for n in nums2:
#             if n in countsd2:
#                 countsd2[n] += 1
#             else:
#                 countsd2[n] = 1

#         res = []
#         for n in countsd1:
#             if n in countsd2:
#                 res = res + [n]* min(countsd2[n], countsd1[n])
                
#         return res
    
#         # Memory: O(2n)
        
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()  # O(n log(n)) 
        nums2.sort()  # + O(m log(m))
        idx1 = 0  # bounded by len(nums1)
        idx2 = 0  # bounder by len(nums2)
        
        res = []
        # + O(2n)
        while idx1 < len(nums1) and idx2 < len(nums2):
            tmpca = 0
            tmpcb = 0
            cn = nums1[idx1]
            
            while idx2 < len(nums2) and nums2[idx2] < cn:
                idx2 += 1
                
            while idx2 < len(nums2) and nums2[idx2] == cn:
                tmpca += 1
                idx2 += 1
            while idx1 < len(nums1) and nums1[idx1] == cn:
                tmpcb += 1
                idx1 += 1

            res = res + [cn]*min(tmpca, tmpcb)
            
        return res