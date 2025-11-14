import random

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]  # random pivot swap
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)


if __name__ == "__main__":
    data = [10, 8, 5, 3, 12, 6]
    print("Original:", data)
    randomized_quicksort(data, 0, len(data) - 1)
    print("Sorted:", data)
