# Python program for login attempt

print("Python program for login attempt") 

print("Enter your username and password")

count = 0

while(count < 3):
    usr_name = input("Enter your username: ")
    usr_pass = input("Enter your password: ")
    
    if usr_name == 'elon' and usr_pass == 'Password@123':
        print("Access granted!")
        break
    else:
        print("Sorry! your username or password is incorrect.")
        
        print("Would you like to try again ? ")
        
        yes_no = input("Type Y/n: ")
        if (yes_no == "Y" or yes_no == "y"):    
            count += 1
            # print ("This is your " + str(count) + " attempt!") 
            # print("This is your {} attempt".format(count))
            print("You have {} attempt left!".format(3 - count))
            
        elif(yes_no == "N" or yes_no == "n"):
            print("Thank you! Have a greate time ahead!")
            break
        else:
            print("Please enter valid input!")


    
    
    
    
    
