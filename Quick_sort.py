def quick_sort(l1):
    if len(l1)<=1:
        return l1

    left=[]
    right=[]
    pivot=l1[-1]

    for i in range(len(l1)-1):
        if l1[i]<pivot:
            left.append(l1[i])
        else:
            right.append(l1[i])
    return quick_sort(left)+[pivot]+quick_sort(right)

l1=[43,56,78,1,90,0]
print(quick_sort(l1))