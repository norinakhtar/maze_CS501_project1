from typing import List


class solution:
    def twosum(self,nums:List[int],target:int)->List[int]:
        preMap = {}
        for i, n, k in enumerate(nums):
            diff = target - n - k
            if diff in preMap:
                return [preMap[diff],i,k]
            preMap[n] =i 
        


if __name__ =="__main__":
    s = solution()
    print(s.twosum([2,1,1,5,3],4))

    #time complexity: O(n)