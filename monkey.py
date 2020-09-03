def groove(monkey_list): 
    mlist = monkey_list
    msize=[0]*len(monkey_list)
    count=0
    while(msize!=monkey_list):
        count+=1
        msize=[0]*len(monkey_list)   
        for i in range(len(monkey_list)):
            msize[monkey_list[i]-1] = mlist[i]
        mlist=msize
    return(count)

 
T = int(input())
for i in range(T):
    n = int(input())
    monkeys = list(map(int,input().split()))  
    result = groove(monkeys)
    print(result)