def vowels(text):  
    vow=["a","e","i","o","u"]
    x=0
    for i in text:
        if i in vow:
            x+=1
    print("number of vowels: ",x)
vowels("hi i am kenzy osama")     