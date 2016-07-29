class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        if m<n:
            return self.findMedianSortedArrays(nums2,nums1)
        low_l=low_r=0
        high_l=high_r=m-1
        while low_l<=high_r:
            mid_l=(low_l+low_r)/2
            mid_r=(high_l+high_r+1)/2
            cut1_l=nums1[mid_l]
            cut1_r=nums1[mid_r]
            cut2_l=nums2[(m+n-mid_l-mid_r-2)/2]
            cut2_r=nums2[(m+n-mid_l-mid_r-1)/2]
            if cut1_l>cut2_r:           #shoule move to left
                last_l=high_l=mid_l
                last_r=high_r=mid_r
            elif cut2_l>cut1_r:         #shoule moce t0 right
                low_l=mid_l
                low_r=mid_r
            else:
                return (max(cut1_l,cut2_l)+min(cut1_r,cut2_r))*1.0/2

a=Solution()
print a.findMedianSortedArrays([1],[3,4])
