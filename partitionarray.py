from typing import List

#partition array
class Solution:
#sort array using counting sort
    def countingSort(self,nums:List):
        n = len(nums)
        output= [0]*n
        count = [0]*10
        sum =0
        for i in range(0,n):
            count[nums[i]]= count[nums[i]]+1
        for i in range(1,10):
            count[i] = count[i]+count[i-1]
        i =n-1
        while i>=0:
            output[count[nums[i]]-1]=nums[i]
            count[nums[i]] -=1
            i -=1
            ##partition implemenation
        for i in range(0,len(output)-1,2):
            sum += output[i]
        return sum




if __name__ =="__main__":
    s = Solution()
    list1= [1,4,3,2]
    list2 = [6,2,6,5,1,2] 
    print("output1: ",s.countingSort(list1))
    print("output2: ",s.countingSort(list2))




