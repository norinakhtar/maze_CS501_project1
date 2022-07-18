from collections import defaultdict
from typing import  List
class Solution:
    def groupAnagrams(self,str:List)-> List[List[str]]:
        result = defaultdict(list)
        for s in str:
            count= [0]*26
            for c in s:
                #asci c= 101 ,a=97,101-97 = 4 , e is at index 4
                count[ord(c)-ord("a") ] +=1
                # print("count",count[ord(c)-ord("a") ])
            result[tuple(count)].append(s)
            # print(result[tuple(count)])
        

        return result.values()



if __name__ == "__main__":
    s = Solution()
    input = ["eat","tea","tan","ate","nat","bat"]
    input2 = [""]
    input3 = ["a"]

    print(s.groupAnagrams(input))
    print(s.groupAnagrams(input2))
    print(s.groupAnagrams(input3))


        













#  dict = {}

#         for s in str:
#             temps = "".join(sorted(s))
#             if temps in dict:
#                 dict[temps].append(s)
#             else:
#                 dict[temps] =[s]
#         return dict.values()