
def count_comparisons_linear_search(arr, target):
    comparisons = 0

    for element in arr:
        comparisons += 1

        if element == target:
            return (True, comparisons)

    return (False, comparisons)


def count_comparisons_binary_search(sorted_arr, target):
    left = 0
    right = len(sorted_arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if sorted_arr[mid] == target:
            return (True, comparisons)

        elif target < sorted_arr[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return (False, comparisons)
