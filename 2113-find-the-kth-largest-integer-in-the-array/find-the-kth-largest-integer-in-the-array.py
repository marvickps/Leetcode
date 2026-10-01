class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        heap = []

        for i in nums:
            num = int(i)
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if int(heap[0])<num:
                    heapq.heappop(heap)
                    heapq.heappush(heap,num)
        
        return str(heap[0])

        # return nums[k-1]
        

