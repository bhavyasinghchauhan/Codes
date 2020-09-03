n=int(input())
b=input().strip()
b=list(b)
g=input().strip()
g=list(g)
if len(b)==n and len(g)==n and n>=1 and n<=10000:
    while True:
        try:
            if b[0]==g[0]:
                b.pop(0)
                g.pop(0)
            elif b[0] in g:
                z=g.pop(0)
                g.append(z)
            elif len(b)==0 or len(g)==0:
                break
            else:
                break
        except :
            break
            
    print(len(b))
#else:
#    print("Invalid")