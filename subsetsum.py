def isSubsetSum(set,n,sum):
    if(sum==0):
        return True
    if (n==0 and sum!=0):
        return False
    if (set[n-1]>sum):
        return isSubsetSum(set ,n-1,sum);
    return isSubsetSum(set ,n-1,sum) or isSubsetSum(set,n-1,sum-set[n-1])

set=[3,34,4,5,12,2]
sum=14
n=len(set)
if (isSubsetSum(set,n,sum)==True):
    print("found")
else:
    print("notfound")

