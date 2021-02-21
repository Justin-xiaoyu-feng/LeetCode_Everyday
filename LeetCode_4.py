# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # similar to merge sort, pop half of the numbers
        l1,l2 = len(nums1), len(nums2)
        
        for i in range((l1+l2)//2):
            if not nums1:
                temp = nums2.pop(0)
            elif not nums2:
                temp = nums1.pop(0)
            elif nums1[0] <= nums2[0]:
                temp = nums1.pop(0)
            else:
                temp = nums2.pop(0)
        if not nums1:
            temp1 = nums2.pop(0)
        elif not nums2:
            temp1 = nums1.pop(0)
        elif nums1[0] <= nums2[0]:
            temp1 = nums1.pop(0)
        else:
            temp1 = nums2.pop(0)
        
        if (l1+l2) % 2 == 1:
            return round(temp1, 5)
        else:
            return round((temp1+temp)/2, 5)