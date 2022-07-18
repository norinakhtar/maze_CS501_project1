
class Solution:
    def partition(self,arr,left,right):
            i =left
            j =right-1
            pivot = arr[right]
            while(i <j ):
                while i < right and arr[i] < pivot:
                    i += 1
                while j > left and arr[j] >= pivot:
                    j -= 1
                if i < j:
                    arr[i],arr[j]= arr[j],arr[i]
            if arr[i]>pivot:
                arr[i],arr[right] = arr[right],arr[i]
            return i

    def quicksort(self,arr,left,right):
        if left < right:
            partition_position= self.partition(arr,left,right)
            self.quicksort(arr,left,partition_position - 1)
            self.quicksort(arr,partition_position + 1,right)
        return arr

        

if __name__ == "__main__":
    s = Solution()
    nums = [5, 2, 3, 1]
    print(s.quicksort(nums,0,len(nums)-1))
            
    


        