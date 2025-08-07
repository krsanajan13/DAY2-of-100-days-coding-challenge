def merge_sort(l1):
    if len(l1)<=1:
        return l1
    mid=len(l1)//2
    left_half=merge_sort(l1[:mid])
    right_half=merge_sort(l1[mid:])
    return  merge(left_half,right_half)
def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res+=left[i:]
    res+=right[j:]
    return res
l1=[56,78,23,1,90,4]
print(merge_sort(l1))