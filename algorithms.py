# Lists of the Algorithms available
class Algos:
    arr = []
    def __init__(self, construct):
        self.construct = construct
        self.set_list(construct.arr)
    def set_list(self, arr):
        self.arr = arr
    
    def insertion_sort(self, ascending=True):
        """Insertion Sort"""
        arr = self.arr
        length = len(arr)
        for i in range(1, length):
            key = arr[i]
            j = i-1
            if ascending:
                while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
                    self.construct.construct_list_bar({j:self.construct.NEON_YELLOW, j+1:self.construct.NEON_GREEN}, True)
                    yield True
            if not ascending:
                while j >= 0 and key > arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
                    self.construct.construct_list_bar({j:self.construct.NEON_YELLOW, j+1:self.construct.NEON_GREEN}, True)
                    yield True
            arr[j + 1] = key
        return arr
    def bubble_sort(self, ascending=True):
        """Bubble Sort Algorithm"""
        arr = self.arr
        length = len(arr)
        
        for i in range(length - 1):
            for j in range((length - 1) - i):
                if ascending:
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        self.construct.construct_list_bar({j:self.construct.NEON_YELLOW, j+1:self.construct.NEON_GREEN}, True)
                        yield True
                if not ascending:
                    if arr[j] < arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        self.construct.construct_list_bar({j:self.construct.NEON_YELLOW, j+1:self.construct.NEON_GREEN}, True)
                        yield True
        return arr
    
    
    def comb_sort(self,ascending = True):
        """Comb Sort"""
        def getNextGap(gap):
            
            gap = (gap * 10)//13
            if gap < 1:
                return 1
            return gap
        arr = self.arr
        n = len(arr)
        
        gap = n
    
        swapped = True
    
        while gap !=1 or swapped == 1:
            gap = getNextGap(gap)
    
            swapped = False
            if ascending:
                for i in range(0, n-gap):
                    if arr[i] > arr[i + gap]:
                        arr[i], arr[i + gap]=arr[i + gap], arr[i]
                        swapped = True
                        self.construct.construct_list_bar({i:self.construct.NEON_YELLOW, i+gap:self.construct.NEON_GREEN}, True)
                        yield True
            else:
                for i in range(0, n-gap):
                    if arr[i] < arr[i + gap]:
                        arr[i], arr[i + gap]=arr[i + gap], arr[i]
                        swapped = True
                        self.construct.construct_list_bar({i:self.construct.NEON_YELLOW, i+gap:self.construct.NEON_GREEN}, True)
                        yield True


    def merge_sort(self, ascending=True):   
        pass
        # if len(self.arr) > 1:
    
        #     # Finding the mid of the array
    
    
        #     # Sorting the first half
        #     self.merge_sort(self.L)
    
        #     # Sorting the second half
        #     self.merge_sort(self.R)
    
        #     i = j = k = 0
    
        #     # Copy data to temp arrays L[] and R[]
        #     while i < len(self.L) and j < len(self.R):
        #         if self.L[i] < self.R[j]:
        #             self.arr[k] = self.L[i]
        #             i += 1
        #         else:
        #             self.arr[k] = self.R[j]
        #             j += 1
                
                
        #         k += 1
        #     # Checking if any element was left
        #     while i < len(self.L):
        #         self.arr[k] = self.L[i]
        #         i += 1
        #         k += 1
                

        #     while j < len(self.R):
        #         self.arr[k] = self.R[j]
        #         j += 1
        #         k += 1

