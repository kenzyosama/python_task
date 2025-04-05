def name_validation(name):
 while name.isalpha:
     print("your name is: ",name)
     break
name_validation('kenzy')     
def email_validation(email): 
 if '@' in email and '.' in email:
     parts=email.split('@')
     username,domain=parts
     if not username:
        print("not valid")
     elif '.' not in domain:
        print("not valid")
     else:
        x,y=domain.split('.')
        if not x or not y:
           print("not valid")
        else:
           print("valid")
 else:
    print("not valid")
email_validation("kenzy@gmail.com")
email_validation("@gmailcom")