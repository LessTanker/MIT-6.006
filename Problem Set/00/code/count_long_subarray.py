def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 1
    ##################
    # YOUR CODE HERE #
    ##################
    max_len = 1
    cur_count = 1
    for i in range(1,len(A)-1):
        if A[i] > A[i-1] :
            cur_count += 1
        else:
            cur_count = 1

        if cur_count > max_len :
            max_len = cur_count
            count = 1
        elif cur_count == max_len:
            count += 1

    return count
