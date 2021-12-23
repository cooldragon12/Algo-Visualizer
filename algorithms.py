# Lists of the Algorithms available
from typing import Tuple


class Algos:
    arr = []
    def __init__(self, construct):
        self.construct = construct
        self.set_list(construct.arr)
    def set_list(self, arr):
        self.arr = arr
    def set_target(self, target):
        self.target = target
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

    def linear_search(self):
        for i in range(len(self.arr)):
            if self.arr[i] == self.target:
                self.construct.construct_list_values({i:self.construct.NEON_GREEN}, True)
                yield i
                return i
                
            self.construct.construct_list_values({i:self.construct.NEON_YELLOW}, True)
            yield i
        return -1
                
    def binary_search(self):
        l = 0
        r = len(self.arr)-1 
        arr = self.arr
        while l <= r:
            mid = l + (r-l) //2
            if self.target == arr[mid]:
                self.construct.construct_list_values({mid:self.construct.NEON_GREEN}, True)
                yield mid
                return mid
            if arr[mid] < self.target:
                l = mid+1
            else:
                
                r = mid-1
            self.construct.construct_list_values({mid:self.construct.NEON_YELLOW, l:self.construct.NEON_BLUE, r:self.construct.NEON_BLUE}, True)
            yield mid
        return -1
