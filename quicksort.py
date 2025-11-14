# Deterministic Quicksort Implementation


def partition(arr, low, high):
    pivot = arr[high]  # deterministic pivot = last element
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


if __name__ == "__main__":
    data = [10, 6, 5, 8, 1, 4]
    print("Original:", data)
    quicksort(data, 0, len(data) - 1)
    print("Sorted:", data)
