
class Solution:
    def sqrt(self,x)->int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right
        
        

if __name__ == "__main__":
    s= Solution()
    x1=4
    x2=8
    print("Square root of 4 is ",s.sqrt(x1))
    print("square root of 8 is ",s.sqrt(x2))

    
             
