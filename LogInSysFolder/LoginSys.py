
import os
import webbrowser



y = ["y", "Y"]


n = ["n", "N"]


os.system("Clear")
loggedIn = bool
PassToAdd = ""
null = None

LoginOrCreate = input("Login Or Create Account: ")

if (LoginOrCreate.__contains__("C") or LoginOrCreate.__contains__("c")):
    #Create Acc
    username = input("Please Create A UserName: ")
    password = input("Please input your desired password: ")
    print("Account Created!")
    file = open("AccsFile.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()

if (LoginOrCreate.__contains__("l") or LoginOrCreate.__contains__("L")):
    
     
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")  
        for line in open("AccsFile.txt","r").readlines(): # Read the lines
            login_info = line.split() # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password == login_info[1]:               
                loggedIn =  True
        if username != login_info[0] and password != login_info[1]:
                if(loggedIn != True):
                    loggedIn =  False   






 



if loggedIn == True:
    print("Logged In!")
    openLoggedInFile = input("Open Logged In File Or Run It? (Open Or Run): ")
    if openLoggedInFile.__contains__("Open") or openLoggedInFile.__contains__("open"):
        webbrowser.open("file:///Users/norber/VSCode/LogInSysFolder/LoggedIn.py")
    elif openLoggedInFile.__contains__("Run") or openLoggedInFile.__contains__("run"):
        os.system('/usr/bin/python3 /Users/norber/VSCode/LogInSysFolder/LoggedIn.py')



    


