def multiplication(x,y):
    s = (((x<0)+(y<0))%2)
    if x==0 or y==0: return 0
    x=x2=abs(x)
    for i in range(abs(y)-1): x2+=x
    return -x2 if s else x2

assert multiplication(3,5)==15
assert multiplication(-4,-8)==32
assert multiplication(-2,6)==-12
assert multiplication(-2,0)==0