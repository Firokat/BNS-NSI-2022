#Dommage pas de while dans les listes par compréhension
def calcul(x):
    out=[]
    while x!=1:
        out.append(x)
        x = int(x/2 if not x%2 else 3*x+1)
    return out+[1]

assert calcul(7)==[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]