class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        if nums1==[] and nums2==[]:
            return 0
        x1 = -1
        x2 = -1
        while (x1+x2+2)<((m+n+1)//2):
            print((m+n+1)//2, x1+x2+2, x1, x2)
            if x1+1<m and x2+1<n:
                if nums1[x1+1] >= nums2[x2+1]:
                    x2+=1
                    answer = nums2[x2]
                else:
                    x1+=1
                    answer = nums1[x1]
            elif x1+1<m:
                x1+=1
                answer = nums1[x1]
            else:
                x2+=1
                answer = nums2[x2]
        
        
        if (m+n)%2==1:
            return answer
        else:
            if x1+1<m and x2+1<n:
                answer2 = min(nums1[x1+1], nums2[x2+1])
            elif x1+1<m:
                answer2 = nums1[x1+1]
            else:
                answer2 = nums2[x2+1]
            
            return (answer+answer2)/2
