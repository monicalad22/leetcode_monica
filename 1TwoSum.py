class Solution:
    def twoSum(self,nums,target):

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                if target == (nums[i] + nums[j]):
                    return [i,j]

obj = Solution()
print(obj.twoSum([2,5,7,15],9))
