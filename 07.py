def conv_bin(x):
    if not x: return ([0], 1)
    out = []
    while x!=0:
        out.append(x%2)
        x//=2
    out.reverse()
    return (out, len(out))

assert conv_bin(9) == ([1,0,0,1],4)