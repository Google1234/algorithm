class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        result=[]
        self.list=nums
        self.quick_sort(0,len(nums)-1)
        pointer1=0
        while pointer1<len(nums)-3 and self.list[pointer1]<=target/4:
            pointer2=pointer1+1
            while pointer2<len(nums)-2 and self.list[pointer2]<=(target-self.list[pointer1])/3:
                pointer3=pointer2+1
                pointer4=len(nums)-1
                need=target-self.list[pointer1]-self.list[pointer2]
                while pointer3<pointer4:
                    t=self.list[pointer3]+self.list[pointer4]
                    if t>need:
                        before=self.list[pointer4]
                        while before==self.list[pointer4] and pointer4>pointer3:
                            pointer4-=1
                    elif t<need:
                        before=self.list[pointer3]
                        while before==self.list[pointer3] and pointer3<pointer4:
                            pointer3+=1
                    else:
                        result.append([self.list[pointer1],self.list[pointer2],self.list[pointer3],self.list[pointer4]])
                        before=self.list[pointer3]
                        while before==self.list[pointer3] and pointer3<pointer4:
                            pointer3+=1
                        before=self.list[pointer4]
                        while before==self.list[pointer4] and pointer4>pointer3:
                            pointer4-=1
                before = self.list[pointer2]
                while before == self.list[pointer2] and pointer2<len(nums)-2:
                    pointer2 += 1
            before = self.list[pointer1]
            while before == self.list[pointer1] and pointer1<len(nums)-3:
                pointer1+= 1
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