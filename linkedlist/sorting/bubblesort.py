a=[23,12,22,45,7,8]
def bubblesort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    print(a)
bubblesort(a)