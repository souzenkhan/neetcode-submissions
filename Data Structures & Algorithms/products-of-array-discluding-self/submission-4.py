class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        prefix_array = [1] * length
        suffix_array = [1] * length 

        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i - 1] * nums[i - 1]

        for i in range(len(nums) -2, -1, -1):
            suffix_array[i] = nums[i + 1] * suffix_array[i + 1]

        return [prefix_array[i] * suffix_array[i] for i in range(length)]

        

        