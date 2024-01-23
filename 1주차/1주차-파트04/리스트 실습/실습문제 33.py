nums=[5,15,2,-8,-12,-29,43,1]
total=0
i=1

for num in nums :
    if i%2!=0 :
        total+=num
    i+=1
print(total)