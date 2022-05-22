RechercheMin = lambda x:list.index(x,min(x))

assert RechercheMin([5])==0
assert RechercheMin([2, 4, 1])==2
assert RechercheMin([5, 3, 2, 2, 4])==2