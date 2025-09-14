def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    m, n, k = len(T), len(S), len(S[0])
    D = {}
    F = [0] * 26
    for i in range(k):
        F[ord(T[i]) - ord('a')] += 1
    key = tuple(F)
    D[key] = D.get(key, 0) + 1
    for i in range(k, m) :
        F[ord(T[i-k]) - ord('a')] -= 1
        F[ord(T[i])-ord('a')] += 1
        key = tuple(F)
        D[key] = D.get(key, 0) + 1
    A = [0] * n
    for i in range(n):
        f = [0] * 26
        for c in S[i] :
            f[ord(c) - ord('a')] += 1
        key = tuple(f)
        if key in D:
            A[i] = D[key]
    return tuple(A)
