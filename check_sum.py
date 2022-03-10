def check_sum(arr, sum):
    l = 0
    r = len(arr)-1

    while (l<r) and (l<len(arr)):
        if arr[l]+arr[r]==sum:
            print(arr[l], arr[r])
            return
        if arr[l]+arr[r]>sum:
            r=r-1
        else:
            l+=1

    print("Sum not possible")
    return    

arr = list(map(int,input("\nEnter the numbers : ").strip().split())) 
sum = int(input("Sum: "))
check_sum(arr, sum)