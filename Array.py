def k largest(arr,k):
arr.sort(reverse=True)
for i in range(k):
print(arr[i],end=" ")
arr = [1,23,12,9,30,2,50]
k=3
k largest(arr,k)
