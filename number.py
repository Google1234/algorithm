class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums=nums
        self.nums.sort()
        self.stop=len(nums)
        self.tmp=[]
        self.result=[]
        self.backtract(0,target,4)
        return self.result
    def backtract(self,start,target,remain_deepth):
        if remain_deepth==2:
            left=start
            right=self.stop-1
            if right>left and self.nums[left]+self.nums[left+1]<=target and self.nums[right]+self.nums[right-1]>=target:
                while left<right:
                    two_sum=self.nums[left]+self.nums[right]
                    if two_sum==target:
                        self.result.append(self.tmp+[self.nums[left],self.nums[right]])
                        left+=1
                        while left<right and self.nums[left]==self.nums[left-1]:
                            left+=1
                        right-=1
                        while right>left and self.nums[right]==self.nums[right+1]:
                            right-=1
                    else:
                        if two_sum<target:
                            left+=1
                        else:
                            right-=1
        else:
            for pointer in range(start,self.stop):
                if pointer+remain_deepth>self.stop:
                    break
                sum=0
                for i in range(1,remain_deepth):
                    sum+=self.nums[pointer+i]
                if sum+self.nums[pointer]>target:
                    break
                sum=0
                for i in range(remain_deepth-1):
                    sum+=self.nums[self.stop-1-i]
                if sum+self.nums[pointer]<target:
                    continue
                if pointer==start or self.nums[pointer]!=self.nums[pointer-1]:
                    self.tmp.append(self.nums[pointer])
                    self.backtract(pointer+1,target-self.nums[pointer],remain_deepth-1)
                    self.tmp.pop()
