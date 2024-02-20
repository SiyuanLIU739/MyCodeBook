# question: given a list of integers, find the interval with maximum sum
#           return sum of this interval

# nums could be replaced by any similar target list
# any similar target list could replace nums
nums = [-1, -1, -1, 23, 1] 
n = len(nums)

# sums is to store prefix sum
# sums[i] = sum(nums[0 ... i]), inclusive
sums = []

# final answer, 0 denots choose no element 
ans = 0

# min of the prefix sum, 0 denotes no elements inside
minSum = 0

for i in range(n):
    # calculate prefix sum
    if(i == 0):
        sums.append(nums[i])
    else:
        sums.append(sums[-1] + nums[i])

    # compare answer with maximum interval sum with interval ends with i
    # minSum is the minimal of sum[0 ... i - 1], inclusive
    ans = max(ans, sums[-1] - minSum)
    minSum = min(minSum, sums[-1])

print(ans)
# as there is only one loop iterating the nums list once
# this algorithm runs in O(n)