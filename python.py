
import os
contact='Contact.txt'
def add_contact():
    fname=input("Enter first name of the contact: ")
    lname=input("Enter last name of the contact: ")
    phno=input("Enter the phone number: ")
    if not phno.isdigit() or len(phno)!=10:
        print("enter valid phone number")
    if check_names(fname,lname):
        print("the names already exists")
    if check_number(phno):
        print("the number already exists")
    if not check_names(fname , lname) and not check_number(phno):
        with open(contact,'a') as file:
            file.write(f'{fname},{lname},{phno}\n')
def display_contact_info():
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=3:
                continue
            fname,lname,phno=parts
            if check_names(fname,lname):
                continue
            if check_number(phno):
                continue
            if not check_names(fname , lname) and not check_number(phno):
                print(f"{fname} {lname}")
                print(f"{phno}")
def check_names(fn,ln):
    if os.path.getsize(contact)==0:
            return False
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=3:
                continue
            fname,lname,_=parts
            if fname==fn and lname==ln:
                return True
    return False
def check_number(ph):
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=3:
                continue
            _, _,phno=parts
            if ph==phno:
                return True
    return False

add_contact()
display_contact_info()
