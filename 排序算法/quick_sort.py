class Solution:
    def quick_sort(self,nums,l,r):
        if l>=r:
            return
        i = l
        j = r
        pivot = nums[(l+r)//2]
        while i<j:
            while nums[i]<pivot:
                i+=1
            while nums[j]>pivot:
                j-=1
            if i<=j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        self.quick_sort(nums,l,j)
        self.quick_sort(nums,i,r)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
