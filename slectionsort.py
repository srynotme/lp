

def selectionsort(a):

    for i in range (len(a)-1):
        min_index=i
        for j in range(i,len(a)):
            if a[min_index]>a[j]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]

        print(a)

    

a=[1,3,5,7,2,9,0]

print("Unsorted arry")
selectionsort(a)
print("Sorted arry\n",a)

