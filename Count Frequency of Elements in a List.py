d={}
l=[1,1,2,3,1,2,3,4,1]
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for k,v in d.items():
    print(f'{k} is repeated  {v} times')