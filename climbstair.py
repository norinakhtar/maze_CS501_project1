class Solution:
    def climbStairs(self,n:int):
        one , two = 1,1
        for i in range(n-1):
            temp = one
            one = one +two
            two = temp 
        return one

    
if __name__ == "__main__":
    s = Solution()
    input1 = 2
    input2 = 3
    print("Output1: ",s.climbStairs(input1))
    print("Output2: ", s.climbStairs(input2))

