
#function for login
def login_in_system(username, password):

    #checks username and password for correctness
    if username == "crabby" and password == "suhdw243":

        #prompts for age
        age = input("age: ")

        #check if age is <= 12 by converting age to an int
        if int(age) <= 12:

            #displays partial access
            return "underage granted partial access"
        
        else:

            #displays full access
            return "of age granted full access"
        
    #checks if only user name is correct
    elif username == "crabby":

        #displays password is incorrect
        print("password incorrect")
        
        #displays denies access
        return "denied access"
    
    #if username is wrong
    else:
        #display that there is no user with that name
        print("no user with that name")

    return "no access"




#prompts user for username and password
username = input("enter username: ")
password = input("enter password: ")

#prints and calls method
print(login_in_system(username,password))