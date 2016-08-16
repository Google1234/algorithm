class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)==0 or len(nums2)==0:
            return []
        result=[]
        self.list=nums1
        self.quick_sort(0,len(nums1)-1)
        new_nums1=self.list
        del self.list
        self.list=nums2
        self.quick_sort(0,len(nums2)-1)
        new_nums2=self.list
        pointer1=pointer2=0
        while pointer1<len(new_nums1) and pointer2<len(new_nums2):
            if new_nums1[pointer1]<new_nums2[pointer2]:
                pointer1+=1
            elif new_nums1[pointer1]>new_nums2[pointer2]:
                pointer2+=1
            else:
                result.append(new_nums1[pointer1])
                pointer1+=1
                pointer2+=1
        return result
    def quick_sort(self, left, right):
        if left == right:
            return 0
        mid = (left + right) / 2  # [left,mid],(mid,right]
        self.quick_sort(left, mid)
        self.quick_sort(mid + 1, right)
        pointer1 = left
        pointer2 = mid + 1
        pointer = 0
        buff = [self.list[i] for i in range(left, right + 1)]
        while pointer1 <= mid and pointer2 <= right:
            if self.list[pointer1] <= self.list[pointer2]:
                buff[pointer] = self.list[pointer1]
                pointer1 += 1
            else:
                buff[pointer] = self.list[pointer2]
                pointer2 += 1
            pointer += 1
        if pointer1 <= mid:
            while pointer1 <= mid:
                buff[pointer] = self.list[pointer1]
                pointer += 1
                pointer1 += 1
        if pointer2 <= right:
            while pointer2 <= right:
                buff[pointer] = self.list[pointer2]
                pointer2 += 1
                pointer += 1
        for i in range(len(buff)):
            self.list[left + i] = buff[i]