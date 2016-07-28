class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        mid=(m+n)*1.0/2
        if m==0 and n==0:
            return 0
        pointer1=pointer2=count=0
        sum=length=0
        while True:
            if pointer1==m:
                a=float("inf")
            else:
                a=nums1[pointer1]
            if pointer2==n:
                b=float("inf")
            else:
                b=nums2[pointer2]
            if a<b:
                last=a
                pointer1+=1
            else:
                last=b
                pointer2+=1
            count+=1
            if count>=mid :
                if count>mid+1:
                    return sum*1.0/length
                sum+=last
                length+=1