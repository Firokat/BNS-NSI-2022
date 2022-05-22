recherche = lambda x,y:len([i for i in y if i==x])

assert recherche('e', "sciences") == 2
assert recherche('i',"mississippi") == 4
assert recherche('a',"mississippi") == 0