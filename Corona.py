from utilities import check_if_valid
from utilities import check_name
from utilities import check_number
from utilities import check_fever
print("Hello! This program was designed to verify eligibility for COVID-19 test")
user_name = input("first, please enter your full name: ")

if check_name(user_name) == False:
    print("Error! You must enter a valid name.")
else:
    sympt1 = input("Please answer the next questions:\n 1. Have you been in contact with positive COVID-19 patient in the last two weeks?\n (1)Yes\n (2)No\n Choice: ")

    if check_if_valid(sympt1) == False:
        print("Not a valid option.")
    else:
         sympt2 = input("Do you have a dry cough?\n (1)Yes\n (2)No\n Choice: ")
         if check_if_valid(sympt2) == False:
             print("Not a valid option.")
         else:
           sympt3 = input("What is your body temperature?")
           if check_number(sympt3) == False:
                 print("Sorry. That`s not a valid temperature.")

