from typing import List


class Solution:

    def sortColors(self,colors:List[int]):
        left = i = 0
        right = len(colors)-1
        while(i <=right):
            if(colors[i]==0):
                colors[i],colors[left]=colors[left],colors[i]
                left += 1
                i+=1
                
            elif(colors[i]==2):
                colors[i],colors[right] = colors[right],colors[i]
                right -=1
            
            else:
                i += 1
        return colors
    

if __name__ == "__main__":
    nums = [2,0,1]
    s = Solution()
    print(s.sortColors(nums))
   


