a=[3,1,4,1,5,9,2,6]
def rangesumarray(a):
  ar=[]
  sum=0
  for i in a:
    sum+=i
    ar.append(sum)
  return ar
b=(rangesumarray(a))
print((b[5]-b[2-1]))