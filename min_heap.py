# Course: CS261 - Data Structures
# Assignment: 5
# Student: Zaki Ahmed
# Description: Minimum heap data structure implementation.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Parameters: Object
        Returns: n/a
        Description: Adds an object, by creating a node and adding it to the heap.
        """
        # Add node to the end of the da
        self.heap.append(node)

        # Check node against correct previous nodes
        i = self.heap.length() - 1
        j = (i - 1) // 2
        var = self.heap.get_at_index(j)

        while node < var:
            self.heap.swap(i, j)
            i = j
            j = (i - 1) // 2
            if j < 0:
                break
            var = self.heap.get_at_index(j)

    def get_min(self) -> object:
        """
        Parameters: n/a
        Returns: Object
        Description: Returns the value of the minimum heap node.
        """
        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Parameters: n/a
        Returns: Object
        Description: Removes the minimum heap node, restructures the heap, and returns the value of the removed heap node.
        """
        if self.heap.length() <= 0:
            raise MinHeapException

        # Get value at first index, get value at last index
        var = self.get_min()
        last = self.heap.get_at_index(self.heap.length() - 1)

        # Set 0th index to last val
        self.heap.set_at_index(0, last)

        # Remove last val
        self.heap.pop()

        # Initialize indexes, and calculate L and R nodes
        i = 0
        j_left = 2 * i + 1
        j_right = 2 * i + 2

        # Start percolate process
        while True:

            left = None
            right = None
            min = None

            # Step 1 - Check if there is a left
            if j_left < self.heap.length() and self.heap.get_at_index(j_left):
                left = self.heap.get_at_index(j_left)

            # Step 2 - Check if there is a right
            if j_right < self.heap.length() and self.heap.get_at_index(j_right):
                right = self.heap.get_at_index(j_right)

            # Step 3 - Pick the correct min to compare to last val (now percolating through the DA)
            # If L and R exist...
            if left is not None and right is not None:
                if left < right:
                    min = left
                    j = j_left
                if left > right:
                    min = right
                    j = j_right
                if left == right:
                    min = left
                    j = j_left

            # If L exists, but R doesn't...
            if left is not None and right is None:
                min = left
                j = j_left

            # If R exists, but L doesn't...
            if left is None and right is not None:
                min = right
                j = j_right

            # If L and R don't exist...
            if left is None and right is None:
                break

            if min is None:
                break

            # Step 4 - Compare last val (now percolating through the DA) to min. If less, then swap...
            if last > min:
                self.heap.swap(i, j)

            # If last is < min value, no more need for percolating and we can break the loop...
            else:
                break

            # Step 5 - Once swap has taken place, update indexes to continue percolating
            i = j
            j_left = 2 * i + 1
            j_right = 2 * i + 2

        return var

    def build_heap_helper(self, i):
        """
        Parameters: Index
        Returns: n/a
        Description: Helper function to help percolate unsorted values in the heap.
        """
        j_left = 2 * i + 1
        j_right = 2 * i + 2

        last = self.heap.get_at_index(i)

        # Start percolate process
        while True:

            left = None
            right = None
            min = None

            # Step 1 - Check if there is a left
            if j_left < self.heap.length():
                left = self.heap.get_at_index(j_left)

            # Step 2 - Check if there is a right
            if j_right < self.heap.length():
                right = self.heap.get_at_index(j_right)

            # Step 3 - Pick the correct min to compare to last val (now percolating through the DA)
            # If L and R exist...
            if left is not None and right is not None:
                if left < right:
                    min = left
                    j = j_left
                if left > right:
                    min = right
                    j = j_right
                if left == right:
                    min = left
                    j = j_left

            # If L exists, but R doesn't...
            if left is not None and right is None:
                min = left
                j = j_left

            # If R exists, but L doesn't...
            if left is None and right is not None:
                min = right
                j = j_right
                # If L and R don't exist...
            if left is None and right is None:
                break

            if min is None:
                break

            # Step 4 - Compare last val (now percolating through the DA) to min. If less, then swap...
            if last > min:
                self.heap.swap(i, j)

            # If last is < min value, no more need for percolating and we can break the loop...
            else:
                break

            # Step 5 - Once swap has taken place, update indexes to continue percolating
            i = j
            j_left = 2 * i + 1
            j_right = 2 * i + 2

    def build_heap(self, da: DynamicArray) -> None:
        """
        Parameters: Dynamic Array
        Returns: n/a
        Description: Takes in a Dynamic Array and builds a minimum sorted heap.
        """
        # Empty out current heap and replace with proper amount of nodes
        temp = []

        for i in range(da.length()):
            temp.append(da.get_at_index(i))

        self.heap = DynamicArray(temp)

        i = da.length() - 1

        while i >= 0:
            self.build_heap_helper(i)
            i -= 1


# BASIC TESTING
if __name__ == '__main__':
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([5, 3, 1, 2, 18, 15, 20, 0, 40, 15, 13])
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)