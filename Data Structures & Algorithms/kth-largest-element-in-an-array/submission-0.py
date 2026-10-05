class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        for i in nums:
            minHeap.append(i)
        heapq.heapify(minHeap)
        while len(minHeap)>k:
            heapq.heappop(minHeap)
        return minHeap[0]