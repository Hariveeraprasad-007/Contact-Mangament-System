
import os
contact='Contact.txt'
def add_contact():
    fname=input("Enter first name of the contact: ")
    lname=input("Enter last name of the contact: ")
    phno=input("Enter the phone number: ")
    with open(contact,'a') as file:
        file.write(f'{fname},{lname},{phno}\n')
def display_contact_info():
    with open(contact,'r') as file:
        for line in file:
            fname,lname,phno=line.strip().split(',')
            print(f"{fname} {lname}")
            print(f"{phno}")
add_contact()
display_contact_info()
