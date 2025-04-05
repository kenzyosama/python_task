def mario(num):
    for i in range(1,5):
        print( num*' ' + i*'*' )
        num-=1
mario(4)