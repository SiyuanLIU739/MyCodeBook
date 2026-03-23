class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        index1 = -1
        index2 = (m + n) // 2
        if((m + n) % 2 == 0):
            index1 = index2 - 1
        else:
            index1 = index2

        number1 = 0
        number2 = 0
        # cnt should be the index of the last element in the merged list
        cnt = -1
        currentNumber = 0
        i = 0
        j = 0
        while(i < m or j < n):
            cnt += 1
            if(i == m):
                currentNumber = nums2[j]
                j += 1
            elif(j == n):
                currentNumber = nums1[i]
                i += 1
            else:
                if(nums1[i] < nums2[j]):
                    currentNumber = nums1[i]
                    i += 1
                else:
                    currentNumber = nums2[j]
                    j += 1
            
            if(cnt == index1):
                number1 = currentNumber
            if(cnt == index2):
                number2 = currentNumber
            if(cnt > index2):
                break
                
        return (number1 + number2) / 2