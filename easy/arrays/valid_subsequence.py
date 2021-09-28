def is_valid_subsequence(array, sequence):
    array_idx = 0
    seq_idx = 0

    while array_idx < len(array) and seq_idx < len(sequence):
        if array[array_idx] == sequence[seq_idx]:
            seq_idx += 1
        array_idx += 1

    return seq_idx == len(sequence)


print(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
