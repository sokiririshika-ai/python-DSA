a=[1,2,3,4,5]
def traversal(b):
    print('[',end="")
    for i in range(len(b)-1):
      print(b[i],end=", ")
    print(b[-1],end="]")

def insert(val,ind,b):
    c=[0 for i in range(len(b)+1)]
    for i in range(0,ind):
        c[i]=b[i]
    for i in range(ind,len(b)):
        c[i+1]=b[i]
    c[ind]=val
    return c
traversal(a)
a=insert(10,2,a)
print()
traversal(a)
a=insert(20,2,a)
print()
traversal(a)