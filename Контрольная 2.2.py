l=list()
al=int(0)
g=int(0)
fam=str()
fam2=str()
for j in range(8,12):
    f = open('mat_dv.txt', 'r')
    for i in f:
        l=i.split(' ')
        l[2]=int(l[2])
        l[4]=int(l[4])
        l[3]=int(l[3])
        if((l[4]>=al or l[3]>=g) and (l[2]==j)):
            al=l[4]
            g=l[3]
            fam=l[0]+' '+l[1]
    print(fam,j)
    f.close()
print('\n')
f = open('mat_dv.txt', 'r')
for i in f:
    l=i.split(' ')
    l[4]=int(l[4])
    l[3]=int(l[3])
    if((l[3]>=g)):
        g=l[3]
        fam=l[0]+' '+l[1]+' '+l[2]
        if(l[3]==g and l[0]+' '+l[1]+' '+l[2]!=fam):
            fam=fam +' '+l[0]+' '+l[1]+' '+l[2]
    if((l[4]>=al)):
        al=l[4]
        fam2=l[0]+' '+l[1]+' '+l[2]
        if(l[4]==al and l[0]+' '+l[1]+' '+l[2]!=fam2):
            fam2=fam2 +' '+l[0]+' '+l[1]+' '+l[2]
print(fam2)
print(fam)
f.close()
