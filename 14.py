correspond = lambda x,y:(len(x)==len(y) and sum([(x[i]==y[i] or y[i]=='*') for i in range(len(x))])==len(x))
assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False