maxi = lambda x:(max(x), list.index(x, max(x)))
assert maxi([1,5,6,9,1,2,3,7,9,8]) == (9,3)
