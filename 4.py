class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1=len(nums1)
        len2=len(nums2)
        if len1<len2:
            return self.findMedianSortedArrays(nums2,nums1)
        if len1==0:
            return 0
        half=(len1+len2)/2
        i_left=1
        i_right=len1
        if len2==0:
            if len1%2==0:
                return (nums1[half-1]+nums1[half])*1.0/2
            else:
                return nums1[half]
        while i_left<=i_right:
            i=(i_left+i_right)/2
            j=half-i #numbers of (nums1 and nums2 left part)<= numbers of (nums1 and nums2 right part)
            #nums1 i-1=-1 i=len1
            #nums2 j-1<=-1 j>=len2
            if i-1>=0 and i<len1:
                nums1_left=nums1[i-1]
                nums1_right=nums1[i]
            else:
                if i-1<0:
                        return (nums1[0]+nums2[len2-1])*1.0/2
                if i>=len1:
                        return (nums1[len1-1]+nums2[0])*1.0/2

            if j-1>=0 and j<len2:
                nums2_left=nums2[j-1]
                nums2_right=nums2[j]
            else:
                if j-1<0 :
                    nums2_left=nums1_left
                    if j<=len2-1 and j>=0:
                        nums2_right = nums2[j]
                if j>=len2:
                    nums2_right=nums1_right
                    if j-1>=0 and j-1<=len2-1:
                        nums2_left = nums2[j - 1]

            if nums1_left>nums2_right:
                i_right=i-1
            elif nums1_right<nums2_left:
                i_left=i+1
            else:
                if (len1+len2)%2==0:
                    return (max(nums1_left,nums2_left)+min(nums1_right,nums2_right))*1.0/2
                else:
                    return min(nums1_right,nums2_right)

a=Solution()
print a.findMedianSortedArrays([1],[2,3])