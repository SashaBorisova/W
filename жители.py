f=open('Perepis.txt','r')

b=int(input())
d=int(input())
count=0
for i in f:
    y=int(i[-5:])
    if(y<1978):
        count+=1
        print(i[:i.find(' ')])
print(count)
f.close()
h=open('Perepis.txt','r')
for i in h:
    y=int(i[-5:])
    if(b<y<d):
        l=i.split(' ')
        print(i[:i.rfind(' ')],y)
h.close()




