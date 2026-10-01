a=[-1,5,3,2,1,0,7,6]
def avgsliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    maxavg=sum/key
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        avg=sum/key 
        if maxavg<avg:
            maxavg=avg
    print(maxavg)
a=avgsliding(4,a)