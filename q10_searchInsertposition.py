from typing import List
class BinarySearch:
    def searchInsert(self,nums:List[int],target:int):
        left, right = 0, len(nums) - 1
        while left<= right:
              pivot = (left+right)//2
              if nums[pivot] == target:
                  return pivot
              if target > nums[pivot]:
                  left = pivot + 1
              else:
                  right = pivot -1
        return left


if __name__== "__main__":
    b = BinarySearch()
    print("Output: ",b.searchInsert([1,3,5,6],7))



    
    



    