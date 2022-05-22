def occurrence_lettres(x):
    out={}
    for i in x:
        out[i] = out[i]+1 if i in out.keys() else 1
    return out 
assert occurrence_lettres('Hello world !')=={'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}
