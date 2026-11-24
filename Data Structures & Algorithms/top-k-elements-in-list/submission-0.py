class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = dict()
        heap = []
        result = []
        for num in nums:
            if num in occurence:
                occurence[num] +=1
            else:
                occurence[num] = 1
        
        for key,value in occurence.items():
            heapq.heappush(heap, (-value, key))

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result