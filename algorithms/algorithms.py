# Sorting Algorithms
def bubble_sort(arr):
    steps = [arr.copy()]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())
    return steps

def quick_sort(arr):
    steps = [arr.copy()]
    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi-1)
            _quick_sort(arr, pi+1, high)
            steps.append(arr.copy())
    
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr.copy())
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(arr.copy())
        return i + 1
    
    _quick_sort(arr, 0, len(arr) - 1)
    return steps

# Heap Sort
def heap_sort(arr):
    steps = [arr.copy()]
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        steps.append(arr.copy())
    return steps


# Merge Sort
def merge_sort(arr):
    steps = [arr.copy()]
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        steps.append(result.copy())
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        return merge(left, right)

    return merge_sort_recursive(arr)


# Radix Sort
def radix_sort(arr):
    max_digit = max([len(str(i)) for i in arr])
    steps = [arr.copy()]
    for i in range(max_digit):
        count = [0] * 10
        sorted_array = [None] * len(arr)
        for j in range(len(arr)):
            count[(arr[j] // 10**i) % 10] += 1
        for j in range(1, 10):
            count[j] += count[j - 1]
        for j in range(len(arr) - 1, -1, -1):
            sorted_array[count[(arr[j] // 10**i) % 10] - 1] = arr[j]
            count[(arr[j] // 10**i) % 10] -= 1
        steps.append(sorted_array.copy())
    return steps


# Insertion Sort
def insertion_sort(arr):
    steps = [arr.copy()]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())
    return steps


# Selection Sort
def selection_sort(arr):
    steps = [arr.copy()]
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        steps.append(arr.copy())
    return steps


# Counting Sort
def counting_sort(arr):
    steps = [arr.copy()]
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    steps.append(output.copy())
    return steps


# Bucket Sort
def bucket_sort(arr):
    steps = [arr.copy()]
    max_val = max(arr)
    n = len(arr)
    size = max_val // n + 1
    buckets = [[] for _ in range(n)]
    for i in arr:
        j = min(int(i / size), n-1)
        buckets[j].append(i)
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        result += bucket
    steps.append(result.copy())
    return steps


# Searching Algorithms
def binary_search(arr, target):
    steps = []
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        step = {
            'low': low,
            'high': high,
            'mid': mid,
            'current_array': arr.copy()
        }
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            step['found'] = True
            steps.append(step)
            return steps
        step['found'] = False
        steps.append(step)
    return steps

def linear_search(arr, target):
    steps = []
    for i in range(len(arr)):
        step = {
            'index': i,
            'current_array': arr.copy()
        }
        if arr[i] == target:
            step['found'] = True
            steps.append(step)
            return steps
        step['found'] = False
        steps.append(step)
    return steps

# Sentinel Linear Search
def sentinel_linear_search(arr, target):
    arr.append(target)
    steps = []
    for i in range(len(arr)):
        step = {
            'index': i,
            'current_array': arr.copy()
        }
        if arr[i] == target:
            step['found'] = True
            steps.append(step)
            return steps
        step['found'] = False
        steps.append(step)
    return steps

# Meta Binary Search | One-Sided Binary Search
def meta_binary_search(arr, target):
    steps = []
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        step = {
            'low': low,
            'high': high,
            'mid': mid,
            'current_array': arr.copy()
        }
        if target == arr[mid]:
            step['found'] = True
            steps.append(step)
            return steps
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        step['found'] = False
        steps.append(step)
    return steps

# Ternary Search
def ternary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        steps = []
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == target:
            steps.append({'found': True, 'index': mid1, 'current_array': arr.copy()})
            return steps
        elif arr[mid2] == target:
            steps.append({'found': True, 'index': mid2, 'current_array': arr.copy()})
            return steps
        elif target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low, high = mid1 + 1, mid2 - 1
        steps.append({'low': low, 'high': high, 'mid1': mid1, 'mid2': mid2, 'current_array': arr.copy()})
    steps.append({'found': False, 'index': None, 'current_array': arr.copy()})
    return steps

# Jump Search
def jump_search(arr, target):
    steps = []
    n = len(arr)
    step_size = int(n ** 0.5)
    next_index = 0
    while next_index < n and arr[next_index] < target:
        current = min(next_index + step_size, n - 1)
        step = {'current_array': arr.copy(), 'next_index': next_index, 'current': current}
        if arr[current] < target:
            step['found'] = False
            next_index = current + 1
        elif arr[current] == target:
            step['found'] = True
            step['index'] = current
            return [step]
        steps.append(step)
    if next_index < n and arr[next_index] == target:
        return [{
            'found': True,
            'index': next_index,
            'current_array': arr.copy()
        }]
    return [{
        'found': False,
        'index': None,
        'current_array': arr.copy()
    }]

# Interpolation Search
def interpolation_search(arr, target):
    steps = []
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        step = {
            'low': low,
            'high': high,
            'current_array': arr.copy()
        }
        if low == high:
            if arr[low] == target:
                step['found'] = True
                step['index'] = low
                steps.append(step)
                return steps
            else:
                step['found'] = False
                step['index'] = None
                steps.append(step)
                return steps
        mid = low + (high - low) * ((target - arr[low]) // (arr[high] - arr[low]))
        if arr[mid] == target:
            step['found'] = True
            step['index'] = mid
            steps.append(step)
            return steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        step['found'] = False
        steps.append(step)
    steps.append({'found': False, 'index': None, 'current_array': arr.copy()})
    return steps

# Exponential Search
def exponential_search(arr, target):
    steps = []
    if target <= arr[0]:
        step = {'found': False, 'index': None, 'current_array': arr.copy()}
        steps.append(step)
        return steps
    i = 1
    while i < len(arr) and arr[i] <= target // 2 ** i:
        i *= 2
    return meta_binary_search(arr[i // 2:i], target)

# Fibonacci Search
def fibonacci_search(arr, target):
    steps = []
    n = len(arr)
    fib_list = [0, 1]
    while fib_list[len(fib_list) - 1] < n:
        fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
    offset = -1
    while fib_list[offset] > 0:
        i = min(offset + 1, n - 1)
        step = {'current_array': arr.copy(), 'fib': fib_list[offset]}
        if arr[i] < target:
            step['found'] = False
            offset -= 1
        elif arr[i] > target:
            offset += 1
        else:
            step['found'] = True
            step['index'] = i
            steps.append(step)
            return steps
        steps.append(step)
    steps.append({'found': False, 'index': None, 'current_array': arr.copy()})
    return steps