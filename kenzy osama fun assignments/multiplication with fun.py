def multipli(num):
    for i in range(1,num+1):
        for j in range(1,10):
            print(f"{i}*{j}={i*j}")
            if i==j:
                break
multipli(5)