password=""
userName=""
setPass = []
setUserName = []
check = 1

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
      str1 += ele

    # return string
    return str1

while(check == 1):
    name=input("enter name : ")
    password = input("Enter Password")
    if(name in setUserName):
        print("Login Successful")
    else:
        print("Sign Up")
        if(password in setPass):
            print("User Already Exists")
        else:
                name = input("Enter name : ")
                passwordnew = input("Enter Password : ")
                setPass.append(passwordnew)
                setUserName.append(name)
                print(setUserName)
                print(setPass)

    print("Sign up sucessful, press 1 to add more users and 2 to end process ")
    ch = int(input())
    if ch !=1:
        break
        

fw = open("test.txt","a")
fw.writelines(listToString(setUserName) +  ": " + listToString(setPass) + ", ")
fw.close()       
        
        


