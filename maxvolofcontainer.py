n=int(input())
a=list(map(int,input().split(' ')))[:n]
def maxVol(a):
    l=0
    r=len(a)-1
    max_volume=0
    for i in range(len(a)//2):
        height=min(a[l],a[r])
        width=r-l
        volume = height * width
        if volume > max_volume:
            max_volume = volume
        l += 1
        r -= 1
    return max_volume
print(maxVol(a))