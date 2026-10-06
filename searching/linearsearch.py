a=[23,12,22,45,7,8]
def linearsearch(ar,target):
  for i in range(len(ar)):
    if ar[i]==target:
      print(f"{target} is found at {i}")
      return
  print(f"{target} not found")
  return -1

print(linearsearch(a,46))