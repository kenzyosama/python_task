def array(nums):
    arr=[]
    print("enter numbers")
    for i in range(5):
        nums=int(input())
        arr.append(nums)
    asc=sorted(arr)
    des=sorted(arr,reverse=True)
    print(asc,des)
array("1,2,3,4,5")