def binary_search1(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    closest_index = None

    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1
        else:
            closest_index = mid
            high = mid - 1

    if closest_index is not None:
        return iterations, arr[closest_index]
    else:
        return iterations, "not found"

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] >= target:
            high = mid - 1

    upper_bound = arr[low] if low < len(arr) else None

    return iterations, upper_bound

def main():
    sorted_array = [0.1, 0.3, 0.5, 0.7, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    target_value = 1.3

    iterations, upper_bound = binary_search(sorted_array, target_value)

    print(f"Кількість ітерацій: {iterations}")
    print(f"Верхня межа: {upper_bound}")


    if upper_bound is not None:
        print("Element found in array")
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
