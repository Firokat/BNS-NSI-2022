def max_dico(x):
    m=max(x.values())
    for i,v in x.items():
        if v==m: return (i,v)

assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})==('Ada', 201)
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50})==('Alan', 222)
