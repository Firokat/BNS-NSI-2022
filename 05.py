rechercheMinMax = lambda x:{'min': None if not len(x) else min(x), 'max': None if not len(x) else max(x)}
assert rechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert rechercheMinMax([]) == {'min': None, 'max': None}