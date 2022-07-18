# Q20 ==>  451. Sort Characters By Frequency - LC - Medium, Bucket Sort
from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        bucket = [[] for i in range(len(s) + 1)]

        for c, freq in Counter(s).items():
            bucket[freq].append(c)

        for freq in reversed(range(len(bucket))):
            for c in bucket[freq]:
                ans.append(c * freq)

        return ''.join(ans)
    

  
if __name__ == "__main__":
    s = Solution() 
    input1 = "tree"
    input2 = "cccaaa"
    input3 = "Aabb"

    print("Output1: ",s.frequencySort(input1))
    print("Output1: ",s.frequencySort(input2))
    print("Output1: ",s.frequencySort(input3))

