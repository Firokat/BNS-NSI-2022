rendu = lambda x:[x//5, (x%5)//2, ((x%5)%2)]
assert rendu(13)==[2,1,1]
assert rendu(64)==[12,2,0]
assert rendu(89)==[17,2,0]