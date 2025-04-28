
import os
import csv
contact='Contact.txt'
def add_contact():
    fname=input("Enter first name of the contact: ")
    lname=input("Enter last name of the contact: ")
    phno=input("Enter the phone number: ")
    event_name=input("enter the event name: ")
    event_date=input("enter the event date: ")
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
            file.write(f'{fname},{lname},{phno},{event_name},{event_date}\n')
def display_all_contacts():
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=5:
                continue
            fname,lname,phno,event_name,event_date=parts
            print(f"{fname} {lname}")
            print(f"{phno}")
            print(f"{event_name} {event_date}")
def check_names(fn,ln):
    if os.path.getsize(contact)==0:
            return False
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=5:
                continue
            fname,lname,_,_,_=parts
            if fname==fn and lname==ln:
                return True
    return False
def check_number(ph):
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=5:
                continue
            _, _,phno,_,_=parts
            if ph==phno:
                return True
    return False
def search_contact():
    search_name=input("enter the name of the contact: ")
    found=False
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=5:
                continue
            fname,lname,phno,event_name,event_date=parts
            name=f'{fname} {lname}'
            if name==search_name:
                print(f"{fname} {lname}")
                print(f"{phno}")
                print(f"{event_name} {event_date}")
                found=True
        if not found:
            print("Contact not found")
def search_by_number():
    ph=input("please enter the number: ")
    found=False
    if not ph.isdigit() or len(ph)!=10:
        print("enter valid phone number")
        return
    with open(contact,'r') as file:
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=5:
                continue
            fname,lname,phno,event_name,event_date=parts
            if phno==ph:
                print(f"{fname} {lname}")
                print(f"{phno}")
                print(f"{event_name} {event_date}")
                found=True
    if not found:
        print("The contact is not found")
def remove_contact_by_name():
    na=input("enter the full name in {fname} {lname} these format: ")
    found=False
    with open(contact,'r') as file:
        lines =file.readlines()
    with open(contact,'w') as file:
        for line in lines:
            parts=line.strip().split(',')
            if len(parts)==5:
                fname,lname,_,_,_=parts
                name=f'{fname} {lname}'
                if na!=name:
                   file.write(line)
                else:
                   found=True
    if found:
        print("Contact is removed succesfully")
    else:
        print("conatct name is not found")
def remove_contact_by_number():
    ph=input("please enter the phone number: ")
    found=False
    with open(contact,'r') as file:
        lines =file.readlines()
    with open(contact,'w') as file:
        for line in lines:
            parts=line.strip().split(',')
            if len(parts)==5:
                _,_,phno,_,_=parts
                if ph!=phno:
                    file.write(line)
                else:
                    found=True
    if found:
        print("Contact is removed succesfully")
    else:
        print("conatct's number is not found")
def update_contact():
    name_to_update=input("please enter the name({fname} {lname}) of the conatct to be updated: ").strip()
    found=False
    with open(contact,'r') as file:
        lines=file.readlines() 
    with open(contact,'w')  as file:
        for line in lines:
            parts=line.strip().split(',')
            if len(parts)==5:
                fname,lname,_,_,_=parts
                name=f'{fname} {lname}'
                if name==name_to_update:
                    new_fname=input("enetr the new first name: ")
                    new_lname=input("enter the new last name: ")
                    new_phno=input("eneter the new phno number: ")
                    event_name=input("enter the new event name")
                    event_date=input("enter the new event date")
                    if not new_phno.isdigit() or len(new_phno) != 10:
                        print("Enter a valid phone number")
                        return
                    else:
                        file.write(f'{new_fname},{new_lname},{new_phno},{event_name},{event_date}\n')
                        found=True
                else:
                    file.write(line)
    if found:
        print("Contact updated succesfully")
    else:
        print("The name is not found")
csv_file='contacts.csv'
def export_as_csv():
    with open(contact,'r') as file,open(csv_file,'w',new_line='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['First Name','Last Name','Phone Number','Event Name','Event Date'])
        for lines in file:
            parts=lines.strip().split(',')
            if len(parts)==5:
                writer.writerow(parts)
    print("Contact are exported as csv file")
def main():
    while True:
        print("1-Add Contacts")
        print("2-Search Conatcts")
        print("3-Display conatcts")
        print("4-Search By Number")
        print("5-Remove conatct by number")
        print("6-Remove conact by name")
        print("7-Update Contact")
        print("8-Export as csv file")
        print("9-Exit")
        try:
            num=int(input("Please give the number based on above choices: "))
        except ValueError:
            print("enter valid number")
            continue
        if num==1:
            add_contact()
        elif num==2:
            search_contact()
        elif num==3:
            display_all_contacts()
        elif num==4:
            search_by_number()
        elif num==5:
            remove_contact_by_number()
        elif num==6:
            remove_contact_by_name()
        elif num==7:
            update_contact()
        elif num==8:
            export_as_csv()
        elif num==9:
            print("Exiting Contact Manager")
            break
        else:
            print("Please enter the valid number")
main()
