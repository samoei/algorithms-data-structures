def two_number_sum(array, target_sum):
    potential_pair = {}

    for i in array:
        if i in array:
            diff = target_sum - i
            return [i, diff]
        else:
            potential_pair[i] = True
    return []


print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
