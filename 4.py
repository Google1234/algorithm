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
            self.findMedianSortedArrays(nums2,nums1)
        half=(len1+len2)/2
        i_left=1
        i_right=len1
        while i_left<=i_right:
            i=(i_left+i_right)/2
            j=half-i #numbers of (nums1 and nums2 left part)<= numbers of (nums1 and nums2 right part)
            if j<0 or (i>0 and  j<len2 and nums1[i-1]>nums2[j]):
                i_right=i-1
            elif j>len2+1 or (i<len1 and j>1 and nums1[i]<nums2[j-1]):
                i_left=i+1
            else:
                if i_right==1:
                    return (nums1[i_right-1]+nums2[len2-1])*1.0/2
                if i_left==len1:
                    return (nums1[i_left-1]+nums2[0])*1.0/2

                if j==0:
                    min_value_nums2_right = nums2[j]
                    max_value_nums2_left=nums1[i-1]
                elif j==len2:
                    min_value_nums2_right=nums1[i]
                    max_value_nums2_left = nums2[j - 1]
                else:
                    min_value_nums2_right=nums2[j]
                    max_value_nums2_left = nums2[j - 1]
                if (len1+len2)%2==0:
                    return (max(nums1[i-1],max_value_nums2_left)+min(nums1[i]+min_value_nums2_right))*1.0/2
                else:
                    return min(nums1[i],min_value_nums2_right)

a=Solution()
print a.findMedianSortedArrays([],[2,3])