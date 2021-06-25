import heapq
class Heap:
    def __init__(self):
        self.priorityQueue = list()
        
    def push(self, elem):
        heapq.heappush(self.priorityQueue, elem)
        
    def pop(self):
        return heapq.heappop(self.priorityQueue)
    
    def empty(self):
        return True if len(self.priorityQueue) == 0 else False