
import os
contact='Contact.txt'
def add_contact():
    fname=input("Enter first name of the contact: ")
    lname=input("Enter last name of the contact: ")
    phno=input("Enter the phone number: ")
    if not phno.isdigit() or len(phno)!=10:
        print("enter valid phone number")
        return
    if check_names(fname,lname):
        print("the names already exists")
        return
    if check_number(phno):
        print("the number already exists")
        return 
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
def search_contact():
    fn=input("enter the first name of the conatct: ")
    ln=input("enter the lasr name of the conatct: ")
    found=False
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=3:
                continue
            fname,lname,phno=parts
            if fname==fn or lname==ln:
                print(f"{fname} {lname}")
                print(f"{phno}")
                found=True
        if not found:
            print("Contact not found")
def search_by_number():
    ph=input("please enter the number")
    found=False
    if not ph.isdigit() or len(ph)!=10:
        print("enter valid phone number")
        return
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=3:
                continue
            fname,lname,phno=parts
            if phno==ph:
                print(f"{fname} {lname}")
                print(f"{phno}")
                found=True
    if not found:
        print("The contact is not found")

def main():
    while True:
        print("1-Add Contacts")
        print("2-Search Conatcts")
        print("3-Display conatcts")
        print("4-Search By Number")
        print("5-Exit")
        try:
            num=int(input("Please give the number based on above choices"))
        except ValueError:
            print("enter valid number")
            continue
        if num==1:
            add_contact()
        elif num==2:
            search_contact()
        elif num==3:
            display_contact_info()
        elif num==4:
            search_by_number()
        elif num==5:
            print("Exiting Contact Manager")
            break
        else:
            print("Please enter the valid number")
main()
