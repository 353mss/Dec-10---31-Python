#Login system

#Usernames and passwords
username = ("353mss")
password = ("test")

#imports
import time
import os


#Main/Start
print("Welcome.")
print()
time.sleep(0.4)

print("Loading login...")

time.sleep(0.7)

print()
username = input("Please Enter your username: ")
if username == "353mss": #Set as your username
    time.sleep(0.3)
    print("Correct Username.")

else:
        print("Wrong username. Try again later...")
        time.sleep(0.6)
        exit()



print()
password = input("Please Enter your password: ")
if password == "test": #set as your password
    time.sleep(0.3)
    print("Correct Password. Welcome!")
    
else:
    print("Worng Password. Try again later...")
    time.sleep(0.6)
    exit()







    #End



#MADE BY 353mss#0447