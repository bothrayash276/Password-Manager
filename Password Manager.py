import random
serVer = {}
serVerTemp ={}

def serverAdding(user_web, user_mail, user_password):
    serVer[user_web] = [user_mail, user_password]

def RandomPassGen():

    #length of randomSet is 70
    randomSet  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'f', 'l', 'm', 'n', 'o', 'p', 'q',  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W,' 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '*', '&', '(', ')']
    i = 15
    temp_pass = ""
    while i>0:
        j = random.randint(0,69)
        temp_pass = temp_pass + randomSet[j]
        i = i-1
    return temp_pass

def SavingPass():
    with open("savep.txt", 'a') as sp:
        for key, values in serVer.items():
            sp.write(f"{key}: {values} \n")

def removing_colon(string):
    l = len(string)
    tem_str = ""
    for i in range(1, l-1):
        tem_str += string[i]
    return tem_str


def AccessPass():
    with open("savep.txt", 'r') as sp:
        eachLine = sp.readlines()
        for eachCharacter in eachLine:
            dividing = eachCharacter.split(': ')
            mail_pass = dividing[1]
            temp_string = ""
            for i in range(1, (len(mail_pass)-3)):
                temp_string = temp_string + mail_pass[i]
            sep_mail_pass = temp_string.split(", ")
            website = dividing[0]
            email = removing_colon(sep_mail_pass[0])
            password  = removing_colon(sep_mail_pass[1])
            serVerTemp[website] = [email, password]
                
def Editing_Password(access_web, useremail, userpassword):
    with open("savep.txt", 'r') as sp:
        eachLine = sp.readlines()
        for eachCharacter in eachLine:
            dividing = eachCharacter.split(': ')
            mail_pass = dividing[1]
            temp_string = ""
            for i in range(1, (len(mail_pass)-3)):
                temp_string = temp_string + mail_pass[i]
            sep_mail_pass = temp_string.split(", ")
            website = dividing[0]
            email = removing_colon(sep_mail_pass[0])
            password  = removing_colon(sep_mail_pass[1])
            serVerTemp[website] = [email, password]
        serVerTemp[access_web] = [useremail, userpassword]
        with open('savep.txt', 'w') as sp:
            for key, values in serVerTemp.items():
                sp.write(f"{key}: {values} \n")




while True:
    print("\n")
    print("There are the options. Press\n", "Add a New Password --> 1\n", "Add a Ramdomly Generated Password --> 2\n",  "Edit the previous password --> 3\n", "Access Previously added Passwords --> 4\n", "Exit the program --> 5\n")
    userWant = int(input("What you want: "))
    #adding a new password
    if(userWant == 1):
        userWeb = input("Enter the website name: ")
        userMail = input("Enter the Email Address: ")
        userPass = input("Enter the password: ")
        serVer[userWeb] = [userMail, userPass]
        SavingPass()
    # randomly generated password
    elif(userWant == 2):
        userWeb5 = input("Enter the website name: ")
        userMail5 = input("Enter the Email Address: ")
        userPass5 = RandomPassGen()
        print(f"Password Generated: {userPass5}")
        serverAdding(userWeb5, userMail5, userPass5)
        SavingPass()
    # updating the password
    elif(userWant==3):
        userWeb4 = input("Enter the website name you want to update: ")
        userMail4 = input("Enter the Email Address: ")
        userPass4 = input("Enter the password: ")
        Editing_Password(userWeb4, userMail4, userPass4)
    #accessing the previously added passwords
    elif(userWant==4):
        AccessPass()
        userW = input("Enter the website name: ")
        print("Email: " + serVerTemp[userW][0])
        print("Password: " + serVerTemp[userW][1])
    # exiting the program
    elif(userWant==5):
        print("Thank You!")
        break


