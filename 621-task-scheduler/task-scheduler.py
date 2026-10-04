class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        heap = list(Counter(tasks).values())
        heapq.heapify_max(heap)
        res = 0

        while heap:
            n_window = n+1
            temp = []
            i = 0
            
            while heap and i < n_window:
                heap_val = heapq.heappop_max(heap) - 1
                if heap_val > 0:
                    temp.append(heap_val)
                i += 1
        
            for t in temp:
                heapq.heappush_max(heap,t)

            if heap:
                res += n_window
            else:
                res +=i
        return res
            
                

                
                

                




