a=[-1,5,3,2,1,0,7,6]
def sliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    max=0
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        if max<sum:
            max=sum
    print(max)
a=sliding(2,a)