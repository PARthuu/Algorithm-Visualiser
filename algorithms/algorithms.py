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
