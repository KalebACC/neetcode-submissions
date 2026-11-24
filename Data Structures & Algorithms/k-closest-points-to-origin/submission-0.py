
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.hypot(x,y)
            heapq.heappush(minHeap, (distance,point))

        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res

        