nombre_de_mots = lambda x:len([i for i in str.split(x) if not i in ['!','?']])
assert nombre_de_mots('Le point d exclamation est separe !')==6
assert nombre_de_mots('Il y a un seul espace entre les mots !')==9