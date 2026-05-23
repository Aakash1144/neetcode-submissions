import heapq
class MedianFinder:

    def __init__(self):
        self.small_max_heap = []
        self.large_min_heap = []

    def addNum(self, num: int) -> None:
        # add num to small max heap to maintain order
        print("add num ", num)
        heapq.heappush(self.small_max_heap, -num)
        largest_small  =  -heapq.heappop(self.small_max_heap)
        heapq.heappush(self.large_min_heap, largest_small)

        if(len(self.large_min_heap)>len(self.small_max_heap)):
            smallest_large = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -smallest_large)
        print("small_max_heap ",self.small_max_heap)
        print("large_min_heap ",self.large_min_heap)
    def findMedian(self) -> float:
        print("find median")
        print("small_max_heap ",self.small_max_heap)
        print("large_min_heap ",self.large_min_heap)
        if(len(self.small_max_heap)>len(self.large_min_heap)):
            return -self.small_max_heap[0]
        
        return ((-self.small_max_heap[0]) + (self.large_min_heap[0]))/2.0