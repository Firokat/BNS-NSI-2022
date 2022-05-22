moyenne = lambda x:sum([i*j for i,j in x])/sum([j for i,j in x])
assert moyenne([(15,2),(9,1),(12,3)])==12.5