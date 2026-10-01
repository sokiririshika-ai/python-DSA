c=[1,3,-1,-3,5,3,6,7]
li=[]
def append(c,el):
  a=[0 for _ in range(len(c)+1)]
  for i in range(len(c)):
    a[i]=c[i]
  a[-1]=el
  return a

def maximum_subarray(a,k):
    for i in range(k,len(a)+1):
        li.append(maximum(a,i-k,i))
    return li

def maximum(a,st,end):
    max=0
    for i in range(st,end):
        if max<a[i]:
            max=a[i]
    return max

print(maximum_subarray(c,3))