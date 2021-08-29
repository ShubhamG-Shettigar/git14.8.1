def fun1(arr,n,d):
    for i in range(d):
        temp=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=temp
def pr(arr,s):
    for i in range(size):
        print("%d"%arr[i],end=" ")
        
array=[1,2,3,4,5,6,7]
size=7
fun1(array,size,4)
print(pr(array,size))
