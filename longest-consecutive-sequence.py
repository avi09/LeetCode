class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums==[]:
            return 0
        nums = sorted(nums)
        sols = []
        for i in range(len(nums)):
            if sols==[]:
                sols= [[nums[i],1]]
            else:
                flag = True
                for j in range(len(sols)):
                    if nums[i]==sols[j][0] or nums[i]==sols[j][0]+1:
                        sols[j][1]+=abs(nums[i]-sols[j][0])
                        sols[j][0]=nums[i]
                        flag = False
                        break
                if flag:
                    sols+=[[nums[i],1]]
        
        return sorted(sols, key = lambda x:x[1], reverse=True)[0][1]
