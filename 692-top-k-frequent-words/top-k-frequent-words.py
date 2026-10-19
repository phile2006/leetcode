class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        maxHeap = [(-cnt, key) for key, cnt in count.items()]
        heapq.heapify(maxHeap)

        out = []
        for i in range(k):
            c, k = heapq.heappop(maxHeap)
            out.append(k)
        return out