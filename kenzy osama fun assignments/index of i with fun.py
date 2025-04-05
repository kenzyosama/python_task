def index_of_i(text):
    for i in range (len(text)):
        if text[i]=='a':
            print(i)
            return
    print("not found")
index_of_i("how are you") 
index_of_i("hi kenzy") 
index_of_i("hi ahmed")      