class Solution:
    def twoSum(self,nums,target):
        # Using a loop for 1st index position. Keeping 1st index steady at the time of comparing with rest of the index values
        for i in range(len(nums)):
            # Using a loop to compare 1st index with rest indicies starting from 2nd index position
            for j in range(i+1,len(nums)):
                # if target is match with the sum of two indicies
                if target == (nums[i] + nums[j]):
                    return [i,j]

obj = Solution()
print(obj.twoSum([2,5,7,15],9))
