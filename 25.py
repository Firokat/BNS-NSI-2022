animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
            {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
            {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
            {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

selection_enclos = lambda x,y:[i for i in x if i['enclos']==y]

assert selection_enclos(animaux, 5)==[{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

assert selection_enclos(animaux, 2)==[{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]

assert selection_enclos(animaux, 7)==[]