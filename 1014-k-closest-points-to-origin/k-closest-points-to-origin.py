class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        #[1,3],[-2,2]
        heap = []
        for p in points:
            x = p[0]
            y = p[1]
            distance = (x)**2 + (y)**2
            if len(heap) < k:
                heapq.heappush_max(heap,(distance,p))
            else:
                if distance < heap[0][0]:
                    heapq.heappop_max(heap)
                    heapq.heappush_max(heap,(distance,p))
        # ls = []
        return [p[1] for p in heap]
           
        
        # return ls
