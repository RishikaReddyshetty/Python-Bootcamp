# printing the elements of list

mobiles=['iphone','samsung','vivo','realme','nothing']
count=1
for ele in mobiles:
    print(count,ele)
    count+=1



mobiles=['iphone','samsung','vivo','realme','nothing']
for i in range(0,len(mobiles)):
    if i%2==0:
        print(mobiles[i])
