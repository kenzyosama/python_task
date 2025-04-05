def two_sets(limit):
    x=[]
    for i in range(1,limit):
        y=[]
        for j in range(1,limit):
            z=i*j
            y.append(z)
            if i==j:
                break
        x.append(y)
    print(x)
two_sets(5)