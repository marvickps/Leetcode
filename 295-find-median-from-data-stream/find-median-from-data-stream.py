class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []


    def addNum(self, num: int) -> None:
        #64
        #max             #min
        #[1,2,3,5]       #[6,7,9,11,64]

        heapq.heappush_max(self.max, num)
        heapq.heappush(self.min, heapq.heappop_max(self.max))
        if len(self.min)>len(self.max):
            heapq.heappush_max(self.max, heapq.heappop(self.min))


    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return float(self.max[0])
        return (self.max[0] + self.min[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()