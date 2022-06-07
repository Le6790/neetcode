from collections import Counter
from itertools import count
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        print(counter)
        
        most_common_sets = counter.most_common(k)

        most_common = []
        for i in most_common_sets:
            most_common.append(i[0])
        
        return most_common
    
    def topKFrequentOptimized(self, nums, k):
        #Bucket Sort method
        count= {}

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        print("count.itesm: ", count.items())
        for n,c in count.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq)-1, 0, -1):

            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        pass
solution = Solution()

print(solution.topKFrequentOptimized([1,1,1,2,2,3],2))
print("----")
print(solution.topKFrequentOptimized([4,1,-1,2,-1,2,3],2))