# DATA STRUCTURES

# Stack: Last-In-First-Out
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Queue: First-In-First-Out
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Node for LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList: Linear collection
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


# ALGORITHMS

# Bubble Sort: Adjacent swapping
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Quick Sort: Divide & conquer
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Linear Search: Sequential search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# Binary Search: Divided search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


# Insertion Sort: Place elements
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Merge Sort: Divide & merge
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


# TESTING
if __name__ == "__main__":
    # Stack test
    s = Stack()
    s.push(5)
    s.push(10)
    print(s.pop())
    print(s.peek())

    # Queue test
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    print(q.dequeue())
    print(q.peek())

    # LinkedList test
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    print("LinkedList:")
    ll.display()

    # Algorithms tests
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print(quick_sort([64, 34, 25, 12, 22, 11, 90]))
    print(linear_search([64, 34, 25, 12, 22, 11, 90], 12))
    print(binary_search([11, 12, 22, 25, 34, 64, 90], 12))
    print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))
    print(merge_sort([64, 34, 25, 12, 22, 11, 90]))
