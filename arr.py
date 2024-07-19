#arr=[1,2,3,4,5]
#k=4
#first=arr[k-1:]
#second=arr[:k-1]
#print(first+second)


 
'''arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
print(second)
print(first)'''



#Without using concatenation operator
'''arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
first.extend(second)
print(first)'''



arr=[1,2,3,4,5]
k=2
first=arr[k+1:k-2:-1]
second=arr[:k-1]
print(first+second)
#print(first)
print(second)

