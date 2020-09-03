def d2b(m):
    ba=bin(m)
    ba=list(ba)[2:]
    return(ba)
# inputs
N = int(input())
l = input()
g = l.split()
g = [int(i) for i in g]

# finding binary equivalents
m = max(g)
lb=len(d2b(m))

gb=[d2b(i) for i in g]
fin = []
for i in gb:
    if len(i)<lb:
        r=['0']*(lb-len(i))
        i=r+i
        fin.append((i))
    else:
        fin.append(i)
#print(fin)
#print(lb)


#checking bin eq
ctr=0

def num_combo(list1): 
	sublist = [[]] 
	for i in range(len(list1) + 1): 
		for j in range(i + 1, len(list1) + 1): 
			sub = list1[i:j] 
			sublist.append(sub) 
	return(sublist) 
 
fnew=num_combo(fin) 
fbin= []
for i in fnew:
    if i==[]:
        pass
    else:
        rn=[]
        for j in i:
            rn.extend(j)
        fbin.append(rn)

#print(fbin)

for i in fbin:
    if i.count('1')==i.count('0'):
        ctr+=1

ans=list(bin(ctr))[2:]
ans=['0']*(lb-len(ans))+ans
finans=''.join(ans)
print(finans)