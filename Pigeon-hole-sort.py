// pigeon hole sort 
def pigeonhole_sort(arr):
    # Find the maximum and minimum values in the input list
    min_val = min(arr)
    max_val = max(arr)
    # Create an array of pigeonholes
    pigeonholes = [0] * (max_val - min_val + 1)

    # Place elements into pigeonholes
    for num in arr:
        pigeonholes[num - min_val] += 1

    # Reconstruct the sorted list from pigeonholes
    sorted_list = []
    for i, count in enumerate(pigeonholes):
        while count > 0:
            sorted_list.append(i + min_val)
            count -= 1

    return sorted_list

# Example usage:
arr = [8, 3, 2, 7, 4, 6, 8]
sorted_arr = pigeonhole_sort(arr)
print("Sorted array:", sorted_arr)
