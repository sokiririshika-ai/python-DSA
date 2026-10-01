n=int(input())
a=list(map(int,input().split(' ')))[:n]
el=int(input())

def linearsearch(a,el):
  c=[]
  for i in range(len(a)):
    if a[i]==el:
      c=append(c,i)
  print(f'element {el} is found at indices {c}')


def append(a,el):
  c=[0 for _ in range(len(a)+1)]
  for i in range(len(a)):
    c[i]=a[i]
  c[-1]=el
  return c


linearsearch(a,el)