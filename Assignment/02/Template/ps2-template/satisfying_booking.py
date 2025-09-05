def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    if len(R) == 1:
        s, t = R[0]
        return ((1, s, t),)
    mid = len(R) // 2
    R1, R2 = R[:mid], R[mid:]
    B1 = satisfying_booking(R1)
    B2 = satisfying_booking(R2)
    B = merge(B1, B2)
    return B

def merge(B1, B2):
    """合并两个预订计划"""
    if not B1:
        return B2
    if not B2:
        return B1
    
    B = []
    i, j = 0, 0
    n1, n2 = len(B1), len(B2)
    
    # 转换为列表以便修改
    list_B1 = list(B1)
    list_B2 = list(B2)
    
    while i < n1 and j < n2:
        t1, t2 = list_B1[i], list_B2[j]
        k1, s1, e1 = t1
        k2, s2, e2 = t2
        
        if s1 < s2:
            if e1 <= s2:
                # B1完全在B2之前，不相交
                B.append(t1)
                i += 1
            elif s2 <= e1 <= e2:
                # B1和B2重叠，B1结束在B2中间
                if s1 < s2:
                    B.append((k1, s1, s2))
                B.append((k1 + k2, s2, e1))
                # 更新B2为剩余部分
                list_B2[j] = (k2, e1, e2)
                i += 1
            else:  # e1 > e2
                # B1完全包含B2
                if s1 < s2:
                    B.append((k1, s1, s2))
                B.append((k1 + k2, s2, e2))
                # 更新B1为剩余部分
                list_B1[i] = (k1, e2, e1)
                j += 1
                
        elif s1 == s2:
            if e1 == e2:
                # 完全相同的时间区间
                B.append((k1 + k2, s1, e1))
                i += 1
                j += 1
            elif e1 < e2:
                # B1先结束
                B.append((k1 + k2, s1, e1))
                # 更新B2为剩余部分
                list_B2[j] = (k2, e1, e2)
                i += 1
            else:  # e1 > e2
                # B2先结束
                B.append((k1 + k2, s1, e2))
                # 更新B1为剩余部分
                list_B1[i] = (k1, e2, e1)
                j += 1
                
        else:  # s1 > s2
            if e2 <= s1:
                # B2完全在B1之前，不相交
                B.append(t2)
                j += 1
            elif s1 <= e2 <= e1:
                # B2和B1重叠，B2结束在B1中间
                if s2 < s1:
                    B.append((k2, s2, s1))
                B.append((k1 + k2, s1, e2))
                # 更新B1为剩余部分
                list_B1[i] = (k1, e2, e1)
                j += 1
            else:  # e2 > e1
                # B2完全包含B1
                if s2 < s1:
                    B.append((k2, s2, s1))
                B.append((k1 + k2, s1, e1))
                # 更新B2为剩余部分
                list_B2[j] = (k2, e1, e2)
                i += 1
    
    # 添加剩余的部分
    while i < n1:
        B.append(list_B1[i])
        i += 1
    while j < n2:
        B.append(list_B2[j])
        j += 1
    
    # 合并相邻且房间数相同的区间
    if not B:
        return tuple(B)
        
    merged_B = [B[0]]
    for i in range(1, len(B)):
        last_booking = merged_B[-1]
        k_last, s_last, e_last = last_booking
        k_curr, s_curr, e_curr = B[i]
        
        # 如果相邻且房间数相同，合并它们
        if e_last == s_curr and k_last == k_curr:
            merged_B[-1] = (k_last, s_last, e_curr)
        else:
            merged_B.append(B[i])
    
    return tuple(merged_B)