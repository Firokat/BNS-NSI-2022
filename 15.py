nb_repetitions = lambda x,y:len([i for i in y if i==x])
assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5])==3
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R'])==2
assert nb_repetitions(12, [1, '!', 7, 21, 36, 44])==0