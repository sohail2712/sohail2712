#Automatic Teller Machine
import pyttsx3 
atm=pyttsx3.init('sapi5')
voices=atm.getProperty('voices')
atm.setProperty('voice',voices[1].id)
from time import sleep

sleep(5)
print(" ************ STATE BANK OF INDIA ***************")

print("*** Welcome to State Bank of India ***")
atm.say("Welcome to State Bank of India")
atm.runAndWait()



atm.say("Kindly enter your pin")
atm.runAndWait()
pin=input("Enter your Pin: ")


atm.say("Available Options are")
atm.runAndWait()
print('-->> Available options: ')

print("1 -> Services")
atm.say("Option 1: Services")
atm.runAndWait()

print("2 -> Withdrawl")
atm.say("Option 2: Withdrawl")
atm.runAndWait()

print("3 -> Mini Statement")
atm.say("Option 3: Mini Statement")
atm.runAndWait()

print("4 -> Balance Enquiry")
atm.say("Option 4: Balance Enquiry")
atm.runAndWait()

print('--> Please, choose an option')
atm.say("Please, choose an option")
atm.runAndWait()
option=input("Enter your option : ")


if option=='1':
    print("*** SBI Services ***")
    atm.say("You have selected Services")
    atm.runAndWait()
    print("visit www.sbi.com to avail SBI services")
    sleep(10)


elif option=='2':
    print("*** Cash Withdrawl ***")
    atm.say("You have selected Cash Withdrawl")
    atm.runAndWait()
    
    atm.say("Enter the amount")
    atm.runAndWait()
    amount=input("Enter the amount: ")
    
    print("Transaction is being processed...")
    atm.say("Please, wait the transaction is being processed")
    atm.runAndWait()
    sleep(3)
    print("Kindly collect your ",amount,' Rs')
    atm.say('Kindly collect your money')
    atm.runAndWait()
    sleep(3)
    print("Thankyou for visiting State Bank of India")
    atm.say("Thankyou for visiting State Bank of India")
    atm.runAndWait()
    print(" *** Have a nice day ***")
    atm.say("Have a nice day")
    atm.runAndWait()
    sleep(5)

elif option=='3':
    print("*** Mini Statement ***")
    atm.say("You have selected Mini Statement")
    atm.runAndWait()
    print("Onscreen Mini Statement is being prepared...")
    atm.say("Your onscreen mini statement is being prepared")
    atm.runAndWait()
    sleep(3)
    print("--> Statement : ")
    print('Your previous withdrawls')
    print('''20/6/22       10000.00 Rs\n26/2/22       18000.00 Rs\n2/7/22       25000.00 Rs\n6/7/22     38000.00 Rs\n13/7/22        23000.00 Rs''')
    atm.say('These are the past five withdrawls, that you have done from savings account sir.')
    atm.runAndWait()
    sleep(5)
    print("Thankyou for visiting State Bank of India")
    atm.say("Thankyou for visiting State Bank of India")
    atm.runAndWait()
    print(" *** Have a nice day ***")
    atm.say("Have a nice day")
    atm.runAndWait()
    sleep(10)

elif option=='4':
    print(" *** Balance Enquiry ***")
    atm.say("You have selected Balance Enquiry")
    atm.runAndWait()
    print("Available balance in your SBI account is 50000 Rs")
    atm.say("Your available balance in your SBI account is 50000 Rs")
    sleep(3)
    print("Thankyou for visiting State Bank of India")
    atm.say("Thankyou for visiting State Bank of India")
    atm.runAndWait()
    print(" *** Have a nice day ***")
    atm.say("Have a nice day")
    atm.runAndWait()
