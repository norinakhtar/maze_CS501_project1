
from typing import List

class Solution:
	def majElement(self,nums:List[int]):
		maxcount = len(nums)//2
		# Traverse through all array elements
		for i in range(len(nums)):
			count=0
			min_idx = i
			for j in range(i, len(nums)):
				if nums[min_idx] > nums[j]:
					min_idx = j
			
				if(nums[j]==nums[i]):
					count +=1
		   
			if (count > maxcount):
				return nums[j]
			    
		return -1
			
			
	
if __name__ == "__main__":
	s = Solution()
	list1=[3,2,3]
	list2=[2,2,1,1,1,2,2]
	print("Output1:",s.majElement(list1))
	print("Output2: ",s.majElement(list2))






