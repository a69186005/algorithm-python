class Array: 
    def __init__(self, arr=None, capacity=10):
        if isinstance(arr, list): 
            self._data = arr[:]
            self._size = len(arr)
            return
        self._data = arr[None]*capacity
        self._size = 0
    
    def getSize(self):
        return self._size
    
    def getCapacity(self):
        return len(self._data)
    
    def isEmpty(self):
        return self._size == 0
    
    ## 
    # Move the data from back to front
    ##  
    def add(self, index, e):

