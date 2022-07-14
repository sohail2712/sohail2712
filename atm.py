# Automatic Teller Machine
import pyttsx3
from time import sleep

atm = pyttsx3.init('sapi5')
voices = atm.getProperty('voices')
atm.setProperty('voice', voices[1].id)


def atm_says(txt, *, wait=.01):
    atm.say(txt)
    atm.runAndWait()
    sleep(wait)

def show_options(num, option):
    print(f"{num} -> {option}")
    atm_says(f"Option {num}: {option}")

def say_bye(*, wait=0):
    print("Thankyou for visiting State Bank of India")
    atm_says("Thankyou for visiting State Bank of India")
    print(" *** Have a nice day ***")
    atm_says("Have a nice day", wait=wait)

def services():
    print("*** SBI Services ***")
    atm_says("You have selected Services")
    print("visit www.sbi.com to avail SBI services")
    sleep(10)

def cash_withdrawl():
    print("*** Cash Withdrawl ***")
    atm_says("You have selected Cash Withdrawl")

    atm_says("Enter the amount")
    amount = input("Enter the amount: ")

    print("Transaction is being processed...")
    atm_says("Please, wait the transaction is being processed", wait=3)

    print(f"Kindly collect your {amount} Rs")
    atm_says('Kindly collect your money', wait=3)
    say_bye(wait=5)

def mini_statement():
    print("*** Mini Statement ***")
    atm_says("You have selected Mini Statement")
    print("Onscreen Mini Statement is being prepared...")
    atm_says("Your onscreen mini statement is being prepared", wait=3)

    print("--> Statement : ", "Your previous withdrawls", sep='\n')
    statement = {"20/06/22": 10000, "26/02/22": 18000, "02/07/22": 25000,
                 "06/07/22": 38000, "13/07/22": 23000.5}
    for k, v in statement.items():
        print(f"{k} - {v:15.2f} Rs")
    atm_says('These are the past five withdrawls, that you have done from savings account sir.', wait=5)
    say_bye(wait=10)

def balance_enquiry():
    print(" *** Balance Enquiry ***")
    atm_says("You have selected Balance Enquiry")
    print("Available balance in your SBI account is 50000 Rs")
    atm_says("Your available balance in your SBI account is 50000 Rs")
    say_bye()

ATM = {"1": services, "2": cash_withdrawl, "3": mini_statement, "4": balance_enquiry}
options = ["Services", "Withdrawl", "Mini Statement", "Balance Enquiry"]

sleep(5)
print(" ************ STATE BANK OF INDIA ***************")
print("*** Welcome to State Bank of India ***")
atm_says("Welcome to State Bank of India")

atm_says("Kindly enter your pin")
pin = input("Enter your Pin: ")

atm_says("Available Options are")
print('-->> Available options: ')

for i, option in enumerate(options):
    show_options(i + 1, option)

print('--> Please, choose an option')
atm_says("Please, choose an option")
option = input("Enter your option : ")
ATM[option]()
