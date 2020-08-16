def find_closest_num(A, target):
    if len(A) == 0:
        return None
    elif len(A) == 1:
        return A[0]

    closest_num = None
    min_difference = float("inf") 
    low = 0
    high = len(A) - 1

    while low <= high:

        mid = (low + high) // 2

        if mid > 0:
            left_min_diff = abs(A[mid-1] - target)

        if mid + 1 < len(A):
            right_min_diff = abs(A[mid+1] - target)

        if left_min_diff < min_difference:
            min_difference = left_min_diff
            closest_num = A[mid-1]
        if right_min_diff < min_difference:
            min_difference = right_min_diff
            closest_num = A[mid+1]

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            return A[mid]

    return closest_num

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]

print(find_closest_num(A1, 8))
print(find_closest_num(A2, 4))
                    