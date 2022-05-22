def recherche(x,y):
    l=0
    r=len(x)-1
    while l<=r:
        m=(l+r)//2
        if x[m]==y: return m
        if m<y: l=m+1
        else: r=m-1
    return -1
assert recherche([2, 3, 4, 5, 6], 5)==3
assert recherche([2, 3, 4, 6, 7], 5)==-1
