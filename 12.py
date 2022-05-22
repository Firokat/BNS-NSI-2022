moyenne = lambda x:sum(x)/len(x) if len(x)!=0 else 'erreur'
assert moyenne([5,3,8]) == 5.333333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert moyenne([]) =='erreur'