class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        self.list=nums
        #quick sort
        self.quick_sort(0,len(nums)-1)
        #print self.list
        triple=[]
        pointer1=0
        pointer2=1
        pointer3=len(self.list)-1
        need=0-self.list[pointer1]
        while pointer1<=(len(self.list)-3):
            while pointer2<pointer3:
                if self.list[pointer2]+self.list[pointer3]>need:
                    t=self.list[pointer3]
                    while pointer3>pointer2 and self.list[pointer3]==t :
                        pointer3-=1
                elif self.list[pointer2]+self.list[pointer3]<need:
                    t=self.list[pointer2]
                    while pointer3>pointer2 and self.list[pointer2]==t :
                        pointer2+=1
                else:
                    triple.append([self.list[pointer1],self.list[pointer2],self.list[pointer3]])
                    t=self.list[pointer2]
                    while pointer3>pointer2 and self.list[pointer2]==t :
                        pointer2+=1
                    t=self.list[pointer3]
                    while pointer3>pointer2 and self.list[pointer3]==t :
                        pointer3-=1
            t = self.list[pointer1]
            while pointer1<=(len(self.list)-3) and self.list[pointer1] == t:
                pointer1+=1
            pointer2=pointer1+1
            pointer3=len(self.list)-1
            need = 0 - self.list[pointer1]
        return triple
    def quick_sort(self,left,right):
        if left==right:
            return 0
        mid=(left+right)/2 #[left,mid],(mid,right]
        self.quick_sort(left,mid)
        self.quick_sort(mid+1,right)
        pointer1=left
        pointer2=mid+1
        pointer=0
        buff=[self.list[i] for i in range(left,right+1)]
        while pointer1<=mid and pointer2<=right:
            if self.list[pointer1]<=self.list[pointer2]:
                buff[pointer]=self.list[pointer1]
                pointer1+=1
            else:
                buff[pointer]=self.list[pointer2]
                pointer2+=1
            pointer+=1
        if pointer1<=mid:
            while pointer1<=mid :
                buff[pointer]=self.list[pointer1]
                pointer+=1
                pointer1+=1
        if pointer2<=right:
            while pointer2<=right:
                buff[pointer]=self.list[pointer2]
                pointer2+=1
                pointer+=1
        for i in range(len(buff)):
            self.list[left+i]=buff[i]